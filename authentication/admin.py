from django.contrib import admin

# Register your models here.
from .models import User,Notification

admin.site.site_header = 'Descussion Froum'
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'auth_provider', 'created_at']
admin.site.register(User, UserAdmin)
@admin.register(Notification)
class notifcation_admin(admin.ModelAdmin):
    list_display=['user','title','first_name']
    def first_name(self, obj):
        if(obj.user):
            return obj.user.email


        return 'No ' 
    first_name.admin_order_field  = 'user'  #Allows column order sorting
    first_name.short_description = 'email'