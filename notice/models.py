from django.db import models
from django.utils import timezone
from authentication.models import User

from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save
# Create your models here.

class Notice(models.Model):
    title = models.CharField(max_length = 500,blank=False,null=False)
    content =RichTextUploadingField(blank=False,null=False, config_name='special')
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='notice')
    date_posted = models.DateTimeField(default=timezone.now)
    slug=models.SlugField(blank=True,null=True,unique=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('notice_detail', kwargs={'slug': self.slug},)
    class Meta:
        ordering = ['-date_posted']
   

# singal to  create unique slug


def notice_pre_save(sender,instance,*arg,**kwargs):
    if instance.slug is None:
        slugify_instance(instance,save=False)

pre_save.connect(notice_pre_save,sender=Notice)


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