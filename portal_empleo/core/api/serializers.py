from core.models import *
from rest_framework import serializers

class AuthUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name','email','password']


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length = 150)
    password = serializers.CharField(max_length = 128)
    
class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offers
        exclude = ['creation_date', 'update_date', 'updater_user', 'creator_user']
        extra_kwargs = {
            'status':{'read_only':True},
        }

class PostulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postulation
        fields = ['offer']

class UserAppSerializer(serializers.ModelSerializer):
    user = AuthUserSerializer()
    
    class Meta:
        model = UserApp
        fields = '__all__'


        