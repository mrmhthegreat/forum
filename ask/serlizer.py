from rest_framework import serializers

from .models import *
from user.serlizer import UserSerializer


class TagSerialzer(serializers.Serializer):
    name=serializers.CharField(read_only=True)
    slug=serializers.CharField(read_only=True)

class TopicSerialzer(serializers.Serializer):
    topic=serializers.CharField(read_only=True)
    id=serializers.IntegerField(read_only=True)
    

class AnswereplySerialzer(serializers.ModelSerializer):
    author=UserSerializer()
    class Meta:
        model=Answer_Reply
        fields=['author','upvote','downvote','date_posted','reply']
        

class AnswerSerialzer(serializers.ModelSerializer):
    author=UserSerializer()
    reply=AnswereplySerialzer(many=True)
    class Meta:
        model=Answer
        fields=['author','answer','reply','upvote','downvote','date_posted','total_reply','is_anonymous','pin_answer']

class PostSelizer(serializers.ModelSerializer):
    url=serializers.HyperlinkedIdentityField(view_name='post_detail',lookup_field='slug')
    editurl=serializers.HyperlinkedIdentityField(view_name='post_update',lookup_field='slug')
    tag=TagSerialzer()
    topics=TopicSerialzer(many=True)
    post_answer= AnswerSerialzer(many=True)

    # getmy-d(sle,d):
    # re {
    #     'objs'
    # }
    # y=serl(sources='rea)
    # usr.em
    author=UserSerializer()
    class Meta:
        model=Post
        fields=['url','editurl','question','topics','content','image','tag','author','upvote','downvote','total_answer','is_active','is_anonymous','date_posted','post_answer']


        
class PostCreateSelizer(serializers.ModelSerializer):
    class Meta:
        model=Post

        fields=['question','topics','content','image','upvote','downvote','total_answer','is_active','is_anonymous','date_posted']

class PostUpdateSelizer(serializers.ModelSerializer):
    class Meta:
        model=Post

        fields=['question','topics','content','image','is_active',]


class PostDetailSelizer(serializers.ModelSerializer):
    
    tag=TagSerialzer()
    topics=TopicSerialzer(many=True)
    
    class Meta:
        model=Post
        fields=['question','topics','content','image','tag','author','upvote','downvote','total_answer','is_active','is_anonymous','date_posted']
     
    # def get_discount(self,obj):
    #     return ''
    # def create(self, validated_data):
    #     a=validated_data.pop('')
    #     return super().create(validated_data)
    # def validate(self, attrs):
    #     r=self.context.get('resquest')
    #     serializers.ValidationError('')
    #     return attrs
    # soyre=''

    # from rest_framework.validators import UniqueValidator
#
# class user():
    # userf
    # def getq
    # look_dats
    # lok[]=self.re.from django.conf import settingsqs=supper().get(ar,kw)
    # ret tq.f(**loa)