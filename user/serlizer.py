from .models import Profile
from django.contrib.auth.models import User
from rest_framework import serializers
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [ 'type', 'image', 'is_verified','token']
class UserSerializer(serializers.ModelSerializer):
    
    profile=ProfileSerializer()
    class Meta:
        model = User
        fields = [ 'first_name','username', 'last_name', 'email','is_active','profile']
   
