from core.models import *
from rest_framework import serializers

class AuthUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AuthUser
        exclude=['last_login','is_superuser','is_staff','is_active','date_joined','password']
        extra_kwargs = {
            'password':{'write_only':True}
        }

class UserAppSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, max_length = 15)
    user = AuthUserSerializer()
    
    class Meta:
        model = UserApp
        fields = '__all__'
