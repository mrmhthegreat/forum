from django.contrib import admin
from .models import Post,Answer,Answer_Reply,Topic


admin.site.register(Answer_Reply)
@admin.register(Post)
class post_admin(admin.ModelAdmin):
    list_display=['slug','is_active','upvote','downvote']
    readonly_fields = ["slug"]
@admin.register(Answer)
class answer_admin(admin.ModelAdmin):
    list_display=['author','post_id','total_reply','upvote','downvote']
admin.site.register(Topic)