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
        fields = [ 'first_name','username', 'last_name', 'email','is_active','profile','i_question','i_answer']

class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [  'image', 'is_verified','token']
class UserUpdateSerializer(serializers.ModelSerializer):
    
    profile=ProfileUpdateSerializer()
    class Meta:
        model = User
        fields = [ 'id','username','first_name', 'last_name', 'email','profile',]


class UserQustupdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'i_question','i_answer']




class UserRegisterSerializer(serializers.Serializer):
    class Meta:
        model = Profile
    def create(self, validated_data):
        image=validated_data.pop('image')
        user=User.objects.create(**validated_data)
        Profile.objects.create(user=user,image=image)
        return super().create(validated_data)
    