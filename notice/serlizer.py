from rest_framework import serializers

from .models import *
from user.serlizer import UserSerializer




class NoticesSerlizer(serializers.ModelSerializer):
    url=serializers.HyperlinkedIdentityField(view_name='notice_detail',lookup_field='slug')
    author=UserSerializer()
    class Meta:
        model=Notice
        fields=['url','title','content','author','image','date_posted']


class PostCreateSelizer(serializers.ModelSerializer):
    class Meta:
        model=Notice
        fields=['title','content','image']
