from rest_framework import generics
from.serlizer import NoticesSerlizer, NoticeCreateSelizer
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
    serializer_class=NoticeCreateSelizer
    queryset=Notice.objects.all()
    def perform_create(self, serializer):
        # serializer.is_valid(raise)
        print(self.request)
        serializer.save(author=self.request.user)
        return super().perform_create(serializer)
    


