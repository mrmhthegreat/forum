from django.contrib import admin

# Register your models here.
from .models import FAQ,FaqTopic
admin.site.register(FaqTopic)
@admin.register(FAQ)
class faq_admin(admin.ModelAdmin):
    list_display=['slug','tag']
    readonly_fields = ["slug"]
