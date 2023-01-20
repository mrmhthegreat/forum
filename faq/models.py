from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from django.utils import timezone

from django.db.models.signals import pre_save
# Create your models here.

class FaqTopic(models.Model):
    topic = models.CharField(max_length=255)
    def __str__(self):
        return self.topic

class FAQ(models.Model):
    title = models.CharField(max_length = 500)
    content = RichTextUploadingField(blank=True,null=False, config_name='special')
    tag = models.CharField(max_length = 200)
    slug=models.SlugField(blank=True,null=True,unique=True)
    topic=models.ManyToManyField(FaqTopic,related_name='faqtopic', blank=False)
    date_posted = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ['-date_posted']
    def __str__(self):
        return self.title
   



def faq_pre_save(sender,instance,*arg,**kwargs):
    if instance.slug is None:
        slugify_instance(instance,save=False)

pre_save.connect(faq_pre_save,sender=FAQ)

def slugify_instance(instance,save=False,new_slug=None):
    if new_slug is not None:
        slug=new_slug
    else:

        slug=slugify(instance.title)
    Klass=instance.__class__

    qs=Klass.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():
        slug=f"{slug}-{qs.count()+1}"
        return slugify_instance(instance,save=save,new_slug=slug)
    instance.slug=slug
    if save:
        instance.save()
    return instance