from django.urls import  include,path
from .api import AllFaqList,FilterFaqList,FaqDetail
urlpatterns =[
    path('allfaq/',AllFaqList.as_view(),name='faq_list'),
    path('faqserach/',FilterFaqList.as_view(),name='faq_search'),
    path('faq/<slug:slug>/',FaqDetail.as_view(),  name="faq_detail"),
   
]

