from django.urls import  include,path
from .views import AllFaqList,FilterFaqList,FaqDetail,AllFaqTopiList
urlpatterns =[
    path('allfaq/',AllFaqList.as_view(),name='faq_list'),
    path('allfaqtopiclist/',AllFaqTopiList.as_view(),name='AllFaqTopiList'),
    path('faqserach/',FilterFaqList.as_view(),name='faq_search'),
    path('faq/<slug:slug>/',FaqDetail.as_view(),  name="faq_detail"),
   
]

