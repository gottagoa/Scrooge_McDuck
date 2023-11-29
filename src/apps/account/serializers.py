from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField()
    

    class Meta:
        model=User
        exclude=('is_staff', 'is_active', 'is_superuser', 'date_joined')
    

class SuperuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email', 'password']


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["first_name", "last_name", "birthday", "email", "mobile", "avatar"]



