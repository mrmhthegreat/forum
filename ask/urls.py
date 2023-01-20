from django.urls import  path
from .views import AllPostList, PostDetail,AllTopicList,PostCreate,SearchPost,AllAnswerLists,PostUpdate,PostDetelte,AllUsertList,AnswerCountUpdate,PostCountUpdate,AnswerCreate,AnswerRCreate,AnswerRCountUpdate
urlpatterns =[
    path('allpostlist/',AllPostList.as_view(),name='post_list'),
    path('allmypostlist/',AllUsertList.as_view(),name='mypost_list'),
    path('postcreate/',PostCreate.as_view(),name='post_create'),
    path('alltopic/',AllTopicList.as_view(),name='topic_list'),
    path('search/',SearchPost.as_view(),name='search_list'),
    path('post/detail/<slug:slug>/',PostDetail.as_view(),  name="post_detail"),
    path('post/answerlist/',AllAnswerLists.as_view(),  name="post_answerlist"),
    path('postupdate/<slug:slug>/',PostUpdate.as_view(),  name="post_update"),
    path('postdelelte/<slug:slug>/',PostDetelte.as_view(),  name="post_delete"),
    path('post/answer/<int:id>/',AnswerCountUpdate.as_view(),  name="answer_update"),
    path('post/createanswer/<int:id>/',AnswerCreate.as_view(),  name="answer_create"),
    path('post/ranswer/<int:id>/',AnswerRCountUpdate.as_view(),  name="ranswer_update"),
    path('post/createranswer/<int:id>/',AnswerRCreate.as_view(),  name="ranswer_create"),
    path('post/count/<int:id>/',PostCountUpdate.as_view(),  name="post_count_update"),
   
]

