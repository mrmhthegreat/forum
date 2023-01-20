from rest_framework import serializers

from .models import Notice
from authentication.serializers import UserSerializer




class NoticesSerlizer(serializers.ModelSerializer):
    url=serializers.HyperlinkedIdentityField(view_name='notice_detail',lookup_field='slug')
    author=UserSerializer()
    class Meta:
        model=Notice
        fields=['url','title','content','author','image','date_posted']


class NoticeCreateSelizer(serializers.ModelSerializer):
    class Meta:
        model=Notice
        fields=['title','content','image']
