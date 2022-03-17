
from datetime import datetime
from .functions import *
from .serializers import *

from rest_framework.permissions import *
from rest_framework.authtoken.models import Token
from rest_framework.decorators import *
from rest_framework import viewsets,status, generics
from rest_framework.response import Response

from django.contrib.auth.hashers import make_password, check_password

from django.db import transaction


class loginview(generics.CreateAPIView):
    serializer_class = LoginSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = LoginSerializer(data = request.data)
        if serializer.is_valid():
            username = serializer.data['username']
            password = serializer.data['password']
            try:
                #print(username)
                user = User.objects.get(username = username)
            except User.DoesNotExist:
                return Response({'User':'Usuario o contraseña incorrectos'}, status = status.HTTP_400_BAD_REQUEST)

            pwd_valid = check_password(password, user.password)
            
            if not pwd_valid:
                return Response({'User':'Usuario o contraseña incorrectos'}, status = status.HTTP_400_BAD_REQUEST)
            else:
                token, _ = Token.objects.get_or_create(user = user)
                #print(token.key)
                return Response({'token': token.key,
                                'user_id': user.pk},status = status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offers.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = OfferSerializer(data = request.data)
        if serializer.is_valid():
            print(self.request.user.id)
            offer_temp = Offers(title = serializer.data['title'], description = serializer.data['description'],
                                salary = serializer.data['salary'], status = Status.objects.get(id = 1),
                                creator_user = self.request.user,updater_user = self.request.user,creation_date = datetime.now())
            offer_temp.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def perform_update(self, serializer):
        serializer.save(title = serializer.validated_data['title'], description = serializer.validated_data['description'],
                                salary = serializer.validated_data['salary'],updater_user = self.request.user, update_date = datetime.now())

class PostulationViewSet(viewsets.ModelViewSet):
    queryset = Postulation.objects.all().select_related('offer')
    serializer_class = PostulationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def create(self, request, *args, **kwargs):
        serializer = PostulationSerializer(data = request.data)
        if serializer.is_valid():
            if Postulation.objects.filter(offer = Offers.objects.get(id = serializer.data['offer']),user= self.request.user).exists():
                return Response({"Postulation":"usted ya se postulo a esta vacante"}, status = status.HTTP_400_BAD_REQUEST)
            else:
                postulation = Postulation(offer = Offers.objects.get(id = serializer.data['offer']),user= self.request.user, creation_date = datetime.now())
                postulation.save()
                return Response(serializer.data,status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        

#CRUD de usuario
class UserAppViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AuthUserSerializer
    
    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = UserAppSerializer(data = request.data)
        if serializer.is_valid():
            auth_user = serializer.data['user']
            auth_user_temp = User(password = make_password(auth_user['password']),
                            is_superuser=False,username=auth_user['username'],
                            last_name=auth_user['last_name'],
                            email=auth_user['email'],
                            first_name=auth_user['first_name'],
                            is_staff=False,
                            is_active=True)
            
            auth_user_temp.save()
            
            user_app = UserApp(document_number = serializer.data['document_number'],
                                second_name = serializer.data['second_name'],
                                second_lastname = serializer.data['second_lastname'],
                                profession = serializer.data['profession'],
                                profile = serializer.data['profile'],
                                document_type = DocumentType.objects.get(id = serializer.data['document_type']),
                                user =auth_user_temp)
            user_app.save()
            register_mail(auth_user_temp.email)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)