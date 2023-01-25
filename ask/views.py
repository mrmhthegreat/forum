from rest_framework import generics,status
from rest_framework import permissions
from rest_framework.response import Response

from ask.custompermsiion import owner
from.serlizer import AnsweReplyCreatSelizer, AnswerCountSelizer, AnswerRCountSelizer, AnswerSerialzer, AnswetCreateSelizer, PostCountSelizer, PostCreateSelizer, PostSelizer, PostUpdateSelizer,TopicSerialzer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# Serializers define the API representation.
from .models import Answer, Answer_Reply, Post,Topic,PostVoter
class AllPostList(generics.ListAPIView):
    serializer_class=PostSelizer
    # pagination_class=[pagination.LimitOffsetPagination]
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filterset_fields = ['topics__topic','is_active']
    ordering_fields = ['date_posted','upvote','downvote']
    queryset=Post.objects.all()

    
class AllUsertList(generics.ListAPIView):
    serializer_class=PostSelizer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filterset_fields = ['topics__topic','is_active']
    ordering_fields = ['date_posted','upvote','downvote']
    
    def get_queryset(self,*args,**kwargs):
        return Post.objects.filter(author=self.request.user)


class AllAnswerLists(generics.ListAPIView):
    serializer_class=AnswerSerialzer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['date_posted','upvote','downvote']
    def get_queryset(self,*args,**kwargs):
        
        p=Post.objects.get(slug=self.request.GET.get('slug'))
        return Answer.objects.filter(post=p)
class AllTopicList(generics.ListAPIView):
    serializer_class=TopicSerialzer
    queryset=Topic.objects.all()

class PostDetail(generics.RetrieveAPIView):
    serializer_class=PostSelizer
    queryset=Post.objects.all()
    lookup_field='slug'

class PostCreate(generics.CreateAPIView):
    serializer_class=PostCreateSelizer
    queryset=Post.objects.all()
    permission_classes=[permissions.IsAuthenticated]
    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)
        serializer.save(author=self.request.user)
        return super().perform_create(serializer)
    
class PostUpdate(generics.UpdateAPIView):
    serializer_class=PostUpdateSelizer
    lookup_field='slug'
    permission_classes=[owner]

    queryset=Post.objects.all()
    def perform_update(self, serializer):
        serializer.is_valid(raise_exception=True)
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


class PostCountUpdate(generics.GenericAPIView):
    serializer_class=PostCountSelizer
    permission_classes=[permissions.IsAuthenticated]  
    def post(self,request,slug):
        answer = request.data
        serializer = self.serializer_class(data=answer)
        serializer.is_valid(raise_exception=True)
        try:
            p=Post.objects.get(slug=id)
            if answer['upvote']==1:
                pt=PostVoter.objects.filter(author=request.user)
                if pt.count()>0:
                    p.voter_up.add(pt[0])
                else:
                    pv=PostVoter(author=request.user)
                    pv.save()
                    p.voter_up.add(pv)
                pv.save()
                p.voter_up.add(pv)
                p.upvote=p.upvote+1
                if p.voter_down.filter(author=request.user).count():
                    p.downvote=p.downvote-1
                    p.voter_down.remove(p.voter_down.filter(author=request.user)[0])
            elif answer['downvote']==1:
                pt=PostVoter.objects.filter(author=request.user)
                if pt.count()>0:
                    p.voter_down.add(pt[0])
                else:
                    pv=PostVoter(author=request.user)
                    pv.save()
                    p.voter_down.add(pv)

                p.downvote=p.downvote+1
                if p.voter_up.filter(author=request.user).exists():
                    p.upvote=p.upvote-1
                    a=p.voter_up.filter(author=request.user)[0]
                    p.voter_up.remove(a)
            elif answer['total_answer']==1:
                p.total_reply= p.total_reply+1
            elif answer['is_active']:
                p.is_active= answer['is_active']
            p.save()
        
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': 'Invalid'}, status=status.HTTP_400_BAD_REQUEST)


class AnswerCountUpdate(generics.GenericAPIView):
    serializer_class=AnswerCountSelizer
    permission_classes=[permissions.IsAuthenticated]
    def post(self,request,id):
        answer = request.data
        serializer = self.serializer_class(data=answer)
        serializer.is_valid(raise_exception=True)
        try:
            p=Answer.objects.get(id=id)
            if answer['upvote']==1:
                pt=PostVoter.objects.filter(author=request.user)
                if pt.count()>0:
                    p.voter_up.add(pt[0])
                else:
                    pv=PostVoter(author=request.user)
                    pv.save()
                    p.voter_up.add(pv)
                pv.save()
                p.voter_up.add(pv)
                p.upvote=p.upvote+1
                if p.voter_down.filter(author=request.user).count():
                    p.downvote=p.downvote-1
                    p.voter_down.remove(p.voter_down.filter(author=request.user)[0])
            elif answer['downvote']==1:
                pt=PostVoter.objects.filter(author=request.user)
                if pt.count()>0:
                    p.voter_down.add(pt[0])
                else:
                    pv=PostVoter(author=request.user)
                    pv.save()
                    p.voter_down.add(pv)

                p.downvote=p.downvote+1
                if p.voter_up.filter(author=request.user).exists():
                    p.upvote=p.upvote-1
                    a=p.voter_up.filter(author=request.user)[0]
                    p.voter_up.remove(a)
            elif answer['total_reply']==1:
                p.total_reply= p.total_reply+1
            elif answer['pin_answer']:
                p.pin_answer= answer['pin_answer']
            p.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': 'Invalid'}, status=status.HTTP_400_BAD_REQUEST)


class AnswerRCountUpdate(generics.GenericAPIView):
    serializer_class=AnswerRCountSelizer
    permission_classes=[permissions.IsAuthenticated]
    def post(self,request,id):
        answer = request.data
        serializer = self.serializer_class(data=answer)
        serializer.is_valid(raise_exception=True)
        try:
            p=Answer_Reply.objects.get(id=id)
            if answer['upvote']==1:
                pt=PostVoter.objects.filter(author=request.user)
                if pt.count()>0:
                    p.voter_up.add(pt[0])
                else:
                    pv=PostVoter(author=request.user)
                    pv.save()
                    p.voter_up.add(pv)
                pv.save()
                p.voter_up.add(pv)
                p.upvote=p.upvote+1
                if p.voter_down.filter(author=request.user).count():
                    p.downvote=p.downvote-1
                    p.voter_down.remove(p.voter_down.filter(author=request.user)[0])
            elif answer['downvote']==1:
                pt=PostVoter.objects.filter(author=request.user)
                if pt.count()>0:
                    p.voter_down.add(pt[0])
                else:
                    pv=PostVoter(author=request.user)
                    pv.save()
                    p.voter_down.add(pv)

                p.downvote=p.downvote+1
                if p.voter_up.filter(author=request.user).exists():
                    p.upvote=p.upvote-1
                    a=p.voter_up.filter(author=request.user)[0]
                    p.voter_up.remove(a)
            p.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': 'Invalid'}, status=status.HTTP_400_BAD_REQUEST)


                                                        
class AnswerCreate(generics.GenericAPIView):
    serializer_class=AnswetCreateSelizer
    permission_classes=[permissions.IsAuthenticated]
    
    def post(self,request,id):
      
        answer = request.data
        serializer = self.serializer_class(data=answer)
        serializer.is_valid(raise_exception=True)
        p=Post.objects.get(id=id)
        serializer.save(author=request.user,post=p)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
class AnswerRCreate(generics.GenericAPIView):
    serializer_class=AnsweReplyCreatSelizer
    permission_classes=[permissions.IsAuthenticated]
    
    def post(self,request,id):
        answer = request.data
        serializer = self.serializer_class(data=answer)
        serializer.is_valid(raise_exception=True)
        p=Answer.objects.get(id=id)
        serializer.save(author=request.user,answer=p)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
                                                                                                                                                                                                                                                            