from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets,generics
from rest_framework import mixins,pagination,permissions,authentication
from rest_framework.reverse import reverse

from ask.custompermsiion import owner
from.serlizer import PostCreateSelizer, PostSelizer, PostUpdateSelizer,TopicSerialzer
from rest_framework import pagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# Serializers define the API representation.
from .models import Post,Topic
class AllPostList(generics.ListAPIView):
    serializer_class=PostSelizer
    # pagination_class=[pagination.LimitOffsetPagination]
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filterset_fields = ['topics__topic','is_active']
    ordering_fields = ['date_posted','upvote','downvote']
    queryset=Post.objects.all()
class AllUsertList(generics.ListAPIView):
    serializer_class=PostSelizer
    # pagination_class=[pagination.LimitOffsetPagination]
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filterset_fields = ['topics__topic','is_active']
    ordering_fields = ['date_posted','upvote','downvote']
    def get_queryset(self,*args,**kwargs):
        return Post.objects.filter(author=self.request.user)

class AllTopicList(generics.ListAPIView):
    serializer_class=TopicSerialzer
    pagination_class=[]
    queryset=Topic.objects.all()

class PostDetail(generics.RetrieveAPIView):
    serializer_class=PostSelizer
    queryset=Post.objects.all()
    lookup_field='slug'

class PostCreate(generics.CreateAPIView):
    serializer_class=PostCreateSelizer
    queryset=Post.objects.all()
    def perform_create(self, serializer):
        # serializer.is_valid(raise)
        print(self.request)
        serializer.save(author=self.request.user)
        return super().perform_create(serializer)
    
class PostUpdate(generics.UpdateAPIView):
    serializer_class=PostUpdateSelizer
    lookup_field='slug'
    permission_classes=[owner]

    queryset=Post.objects.all()
    def perform_update(self, serializer):
        serializer.save()
        return super().perform_update(serializer)
class PostDetelte(generics.DestroyAPIView):
    serializer_class=PostUpdateSelizer
    lookup_field='slug'
    permission_classes=[owner]
    queryset=Post.objects.all()
    def perform_destroy(self, instance):
        print(instance)
        return super().perform_destroy(instance)
   
class SearchPost(generics.ListAPIView):
    serializer_class=PostCreateSelizer
    def get_queryset(self,*args,**kwargs):
        qs=super().get_queryset(*args,**kwargs)
        q=self.request.GET.get('q')
        ac=self.request.GET.get('user')
        us=self.request.GET.get('user')
        results=None
        if us is not None:
            if self.request.user.is_authenticated:
                if ac is not None:
                    results=qs.search(q,user=True,active=True)
                return results
                
            else:
                if ac is not None:
                    results=qs.search(q,active=True)
                return results
            
        if ac is not None:
            results=qs.search(q,active=True)
            return results


        results=qs.search(q)
        return results


# class AlLPOSTLIST(generics.ListCreateAPIView):





                                                                                                                                                                                                                                                                                                                     