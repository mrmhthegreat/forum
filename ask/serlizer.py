from rest_framework import serializers

from .models import *
from authentication.serializers import UserSerializer

class TagSerialzer(serializers.Serializer):
    name=serializers.CharField(read_only=True)
    slug=serializers.CharField(read_only=True)

class TopicSerialzer(serializers.Serializer):
    topic=serializers.CharField(read_only=True)
    image=serializers.CharField(read_only=True)

    id=serializers.IntegerField(read_only=True)
    
class VoteSerialzer(serializers.ModelSerializer):
    email=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=PostVoter
        fields=['email']
    def get_email(self,obj):
        return obj.author.email
class AnswereplySerialzer(serializers.ModelSerializer):
    author=UserSerializer()
    voter_up=VoteSerialzer(many=True)
    voter_down=VoteSerialzer(many=True)
    class Meta:
        model=Answer_Reply
        fields=['id','author','upvote','downvote','date_posted','reply','voter_up','voter_down']
        
class AnswerSerialzer(serializers.ModelSerializer):
    author=UserSerializer()
    reply=AnswereplySerialzer(many=True)
   
    voter_up=VoteSerialzer(many=True)
    voter_down=VoteSerialzer(many=True)
    class Meta:
        model=Answer
        fields=['id','author','answer','reply','upvote','downvote','date_posted','total_reply','is_anonymous','pin_answer','voter_up','voter_down']

class PostSelizer(serializers.ModelSerializer):
    url=serializers.HyperlinkedIdentityField(view_name='post_detail',lookup_field='slug')
    editurl=serializers.HyperlinkedIdentityField(view_name='post_update',lookup_field='slug')
    answer_url=serializers.SerializerMethodField(read_only=True)
    topics=TopicSerialzer(many=True)
    voter_up=VoteSerialzer(many=True)
    voter_down=VoteSerialzer(many=True)
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
        fields=['id','url','editurl','answer_url','question','topics','content','image','author','upvote','downvote','total_answer','is_active','is_anonymous','date_posted','voter_up','voter_down']





        



class PostDetailSelizer(serializers.ModelSerializer):
    
    tag=TagSerialzer()
    topics=TopicSerialzer(many=True)
    voter_up=VoteSerialzer(many=True)
    voter_down=VoteSerialzer(many=True)
    
    class Meta:
        model=Post
        fields=['id','question','topics','content','image','tag','author','upvote','downvote','total_answer','is_active','is_anonymous','date_posted','voter_up','voter_down']
     
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
    class Meta:
        model=Post
        fields=['upvote','downvote','total_answer','is_active']
class AnswerCountSelizer(serializers.ModelSerializer):
    class Meta:
        model=Answer
        fields=['upvote','downvote','total_reply','pin_answer']
class AnswerRCountSelizer(serializers.ModelSerializer):
    class Meta:
        model=Answer_Reply
        fields=['upvote','downvote']

class AnswetCreateSelizer(serializers.ModelSerializer):
    class Meta:
        model=Answer
        fields=['answer','is_anonymous']
class AnsweReplyCreatSelizer(serializers.ModelSerializer):
    class Meta:
        model=Answer_Reply
        fields=['reply']