from django.urls import  path
from .api import GoogleLogin, UserViewSet,UserProfileRegister,UserUpdate,UserProfileUpdate
urlpatterns =[
    path('userdetail/',UserViewSet.as_view(),name='user_detail'),
    path('user/profile/update/<int:id>',UserProfileUpdate.as_view(),name='user_pudate'),
    path('user/update/<int:id>',UserUpdate.as_view(),name='user_update'),
    path('rest-auth/google/', GoogleLogin.as_view(), name='fb_login')
   
]

