from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets,generics
from rest_framework import mixins,pagination,permissions,authentication
from rest_framework.reverse import reverse
from.serlizer import NoticesSerlizer, PostCreateSelizer
from rest_framework import pagination
# Serializers define the API representation.
from .models import Notice

class AllNoticeList(generics.ListAPIView):
    serializer_class=NoticesSerlizer
    # pagination_class=[pagination.LimitOffsetPagination]
    queryset=Notice.objects.all()

class NoticeDetail(generics.RetrieveAPIView):
    serializer_class=NoticesSerlizer
    queryset=Notice.objects.all()
    lookup_field='slug'

class NoticeCreate(generics.CreateAPIView):
    serializer_class=PostCreateSelizer
    queryset=Notice.objects.all()
    def perform_create(self, serializer):
        # serializer.is_valid(raise)
        print(self.request)
        serializer.save(author=self.request.user)
        return super().perform_create(serializer)
    





                                                                                                                                                                                                                                                                                                                     