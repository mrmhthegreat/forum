from django.contrib import admin
from .models import Notice
# Register your models here.
@admin.register(Notice)
class notice_admin(admin.ModelAdmin):
    list_display=['slug','title']
    readonly_fields = ["slug"]
