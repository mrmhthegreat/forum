from django.contrib import admin
from .models import Post,Answer,Answer_Reply,Topic,PostVoter
from django.urls import reverse

from django.utils.html import format_html
admin.site.name='Batak'
@admin.register(PostVoter)
class postv_admin(admin.ModelAdmin):
    list_display=['email']
    def email(Self,obj):
        return obj.author.email
    email.admin_order_field  = 'author'  #Allows column order sorting
    email.short_description = 'Email'
    
@admin.register(Post)
class post_admin(admin.ModelAdmin):
    list_display=['slug','is_active','upvote','downvote']
    readonly_fields = ["slug"]
@admin.register(Answer)
class answer_admin(admin.ModelAdmin):
    list_display=['id','author','poste','total_reply','upvote','downvote','voters']
    def poste(self,obj):
        return obj.post.slug

    poste.admin_order_field  = 'post'  #Allows column order sorting
    poste.short_description = 'Post' 
    poste.allow_tags = True
    def voters(Self,obj):
        return obj.voter_up.count()+obj.voter_down.count()
    voters.admin_order_field  = 'voters'  #Allows column order sorting
    voters.short_description = 'Total Vote' 
    
@admin.register(Answer_Reply)
class answerr_admin(admin.ModelAdmin):
    list_display=['id','reply','author','answer_id','upvote','downvote','voters']
    def voters(Self,obj):
        return obj.voter_up.count()+obj.voter_down.count()
    voters.admin_order_field  = 'voters'  #Allows column order sorting
    voters.short_description = 'Votes'
admin.site.register(Topic)