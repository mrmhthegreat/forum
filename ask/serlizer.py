from rest_framework import serializers

from .models import *
from authentication.serializers import UserSerializer

class TagSerialzer(serializers.Serializer):
    name=serializers.CharField(read_only=True)
    slug=serializers.CharField(read_only=True)

class TopicSerialzer(serializers.Serializer):
    topic=serializers.CharField(read_only=True)
    id=serializers.IntegerField(read_only=True)
    
class VoteSerialzer(serializers.Serializer):
    username=serializers.CharField(read_only=True)
class AnswereplySerialzer(serializers.ModelSerializer):
    author=UserSerializer()
    voter=VoteSerialzer(many=True)
    class Meta:
        model=Answer_Reply
        fields=['id','author','upvote','downvote','date_posted','reply','voter']
        

class AnswerSerialzer(serializers.ModelSerializer):
    author=UserSerializer()
    reply=AnswereplySerialzer(many=True)
    voter=VoteSerialzer(many=True)

    class Meta:
        model=Answer
        fields=['id','author','answer','reply','upvote','downvote','date_posted','total_reply','is_anonymous','pin_answer','voter']

class PostSelizer(serializers.ModelSerializer):
    url=serializers.HyperlinkedIdentityField(view_name='post_detail',lookup_field='slug')
    editurl=serializers.HyperlinkedIdentityField(view_name='post_update',lookup_field='slug')
    answer_url=serializers.SerializerMethodField(read_only=True)
    tag=TagSerialzer()
    topics=TopicSerialzer(many=True)
    voter=VoteSerialzer(many=True)
    def get_answer_url(self,obj):
        return 'http://127.0.0.1:8000'+'/api/v1/postdata/post/answerlist/'+f"?slug={obj.slug}"
    # getmy-d(sle,d):
    # re {
    #     'objs'
    # }
    # y=serl(sources='rea)
    # usr.em
    author=UserSerializer()
    class Meta:
        model=Post
        fields=['id','url','editurl','answer_url','question','topics','content','image','tag','author','upvote','downvote','total_answer','is_active','is_anonymous','date_posted','voter']





        



class PostDetailSelizer(serializers.ModelSerializer):
    
    tag=TagSerialzer()
    topics=TopicSerialzer(many=True)
    voter=VoteSerialzer(many=True)
    
    class Meta:
        model=Post
        fields=['id','question','topics','content','image','tag','author','upvote','downvote','total_answer','is_active','is_anonymous','date_posted','voter']
     
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
class PostCreateSelizer(serializers.ModelSerializer):
    class Meta:
        model=Post

        fields=['question','topics','content','image','is_active','is_anonymous']

class PostUpdateSelizer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=['question','topics','content','image','is_active',]



class PostCountSelizer(serializers.ModelSerializer):
    post=serializers.IntegerField(write_only=True)
    class Meta:
        model=Post
        fields=['post','upvote','downvote','total_answer','is_active']
class AnswerCountSelizer(serializers.ModelSerializer):
    id=serializers.IntegerField(write_only=True)
    class Meta:
        model=Answer
        fields=['upvote','downvote','total_reply','pin_answer','id']
class AnswerRCountSelizer(serializers.ModelSerializer):
    id=serializers.IntegerField(write_only=True)
    class Meta:
        model=Answer_Reply
        fields=['upvote','downvote','id']

class AnswetCreateSelizer(serializers.ModelSerializer):
    post=serializers.IntegerField(write_only=True)
    class Meta:
        model=Answer

        fields=['answer','is_anonymous','post']
class AnsweReplyCreatSelizer(serializers.ModelSerializer):
    anser=serializers.IntegerField(write_only=True)
    class Meta:
        model=Answer_Reply
        fields=['reply','anser']