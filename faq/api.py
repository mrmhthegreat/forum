from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets,generics
from rest_framework import mixins,pagination,permissions,authentication
from rest_framework.reverse import reverse
from.serlizer import FaqSerlizer,TopicSerialzer
from rest_framework import pagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# Serializers define the API representation.
from .models import FaqTopic,FAQ

class AllFaqList(generics.ListAPIView):
    serializer_class=FaqSerlizer
    # pagination_class=[pagination.LimitOffsetPagination]
    queryset=FAQ.objects.all()
  
class FilterFaqList(generics.ListAPIView):
    serializer_class=FaqSerlizer
    # pagination_class=[pagination.LimitOffsetPagination]
    queryset=FAQ.objects.all()
    filter_backends = [filters.SearchFilter,DjangoFilterBackend,filters.OrderingFilter]
    filterset_fields = ['topic__topic']
    search_fields = ['title', 'topic__topic']
    ordering_fields = ['date_posted',]
class FaqDetail(generics.RetrieveAPIView):
    serializer_class=FaqSerlizer
    queryset=FAQ.objects.all()
    lookup_field='slug'



    





                                                                                                                                                                                                                                                                                                                     