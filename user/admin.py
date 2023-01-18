from django.contrib import admin
# Register your models here.
from .models import Notification, Profile

@admin.register(Profile)
class profile_admin(admin.ModelAdmin):
    list_display=['user','is_verified','first_name']
    readonly_fields=['token']
    search_fields = ['type'] 
    list_filter = ['type','is_verified']

    def first_name(self, obj):
        if(obj.user):
            return obj.user.email


        return 'No ' 
    first_name.admin_order_field  = 'user'  #Allows column order sorting
    first_name.short_description = 'email'

@admin.register(Notification)
class notifcation_admin(admin.ModelAdmin):
    list_display=['user','title','first_name']
    def first_name(self, obj):
        if(obj.user):
            return obj.user.email


        return 'No ' 
    first_name.admin_order_field  = 'user'  #Allows column order sorting
    first_name.short_description = 'email'


