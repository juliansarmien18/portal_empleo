from .serializers import *
from rest_framework import viewsets,status
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from django.db import transaction

class UserAppViewSet(viewsets.ModelViewSet):
    queryset = UserApp.objects.all().select_related('user')
    serializer_class = UserAppSerializer
    
    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = UserAppSerializer(data = request.data)
        if serializer.is_valid():
            auth_user = serializer.data['user']

            auth_user = AuthUser(password = make_password(auth_user['password']),
                            is_superuser=False,username=auth_user['username'],
                            last_name=auth_user['last_name'],
                            email=auth_user['email'],
                            first_name=auth_user['first_name'],
                            is_staff=False,
                            is_active=True)
            
            auth_user.save()
            
            user_app = UserApp(document_number = serializer.data['document_number'],
                                second_name = serializer.data['second_name'],
                                second_lastname = serializer.data['second_lastname'],
                                profession = serializer.data['profession'],
                                profile = serializer.data['profile'],
                                document_type = serializer.data['document_type'],
                                user =auth_user)
            user_app.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)