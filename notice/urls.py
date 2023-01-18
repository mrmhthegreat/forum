from django.urls import  include,path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import CreateView
from .api import AllNoticeList,NoticeCreate,NoticeDetail
urlpatterns =[
    path('allnotice/',AllNoticeList.as_view(),name='notice_list'),
    path('noticecreate/',NoticeCreate.as_view(),name='notice_create'),
    path('notice/<slug:slug>/',NoticeDetail.as_view(),  name="notice_detail"),
   
]

