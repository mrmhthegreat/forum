from rest_framework import generics
from.serlizer import FaqSerlizer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# Serializers define the API representation.
from .models import FaqTopic,FAQ

class AllFaqList(generics.ListAPIView):
    serializer_class=FaqSerlizer
    queryset=FAQ.objects.all()
  
class FilterFaqList(generics.ListAPIView):
    serializer_class=FaqSerlizer
    queryset=FAQ.objects.all()
    filter_backends = [filters.SearchFilter,DjangoFilterBackend,filters.OrderingFilter]
    filterset_fields = ['topic__topic']
    search_fields = ['title', 'topic__topic']
    ordering_fields = ['date_posted']
class FaqDetail(generics.RetrieveAPIView):
    serializer_class=FaqSerlizer
    queryset=FAQ.objects.all()
    lookup_field='slug'



    





                                                                                                                                                                                                                                                                                                                     