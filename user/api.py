from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import generics
from ask.custompermsiion import owner
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status,permissions
# Serializers define the API representation.
from.serlizer import UserQustupdateSerializer, UserRegisterSerializer, UserSerializer,User,Profile
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView




class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
class UserViewSet(generics.RetrieveAPIView):
    serializer_class=UserSerializer
    # lookup_field='id'
    permission_classes=[owner,permissions.IsAuthenticated]
    def get_queryset(self,*args,**kwargs):
        return User.objects.filter(author=self.request.user)

class UserUpdate(generics.UpdateAPIView):
    serializer_class=UserQustupdateSerializer
    permission_classes=[owner]
    lookup_field='id'
    def perform_update(self, serializer):
        return super().perform_update(serializer)
 
class UserProfileUpdate(generics.UpdateAPIView):
    serializer_class=UserQustupdateSerializer
    lookup_field='id'
    permission_classes=[owner]
    
    def perform_update(self, serializer):
        return super().perform_update(serializer)
class UserProfileRegister(generics.CreateAPIView):
    serializer_class=UserRegisterSerializer
    queryset=Profile.objects.all()

