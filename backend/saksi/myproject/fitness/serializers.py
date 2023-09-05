from rest_framework import serializers
from .models import CustomUser
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'password','is_trainer','username']
