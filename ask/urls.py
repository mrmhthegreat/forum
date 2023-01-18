from django.urls import  path
from .api import AllPostList, PostDetail,AllTopicList,PostCreate,SearchPost,PostUpdate,PostDetelte
urlpatterns =[
    path('allpostlist/',AllPostList.as_view(),name='post_list'),
    path('postcreate/',PostCreate.as_view(),name='post_create'),
    path('alltopic/',AllTopicList.as_view(),name='topic_list'),
    path('search/',SearchPost.as_view(),name='search_list'),
    path('post/<slug:slug>/',PostDetail.as_view(),  name="post_detail"),
    path('postupdate/<slug:slug>/',PostUpdate.as_view(),  name="post_update"),
    path('postdelelte/<slug:slug>/',PostDetelte.as_view(),  name="post_delete"),

   
]

