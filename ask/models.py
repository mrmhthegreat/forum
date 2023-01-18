from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save,post_save
from taggit.managers import TaggableManager
from django.db.models import Q

class Topic(models.Model):
    topic = models.CharField(max_length=255)
    def __str__(self):
        return self.topic
 
class PostQuerySet(models.QuerySet):
    def is_active(self):
        return self.filter(is_active=True)
    def search(self,query,user=None,active=False):
        lookup=Q(question__icontains=query)|Q(topics__topic__icontains=query)
        
        if active:
            qs=self.is_active.filter(lookup)
            if user is not None:
                qs=qs.filter(author=user)
            return qs
        else:
            qs=self.filter(lookup)
            if user is not None:
                qs2=qs.filter(author=user).filter(lookup)
                qs=(qs|qs2).distinct()
            return qs
class PostManger(models.Manager):
    def get_queryset(self,*args,**kwrgs):
        return PostQuerySet(self.model,using=self._db)

    def search(self,query,user=None,active=False):
        return self.get_querry().search(query,user=user,active=active)
class PostVoter(models.Model):
    author = models.ForeignKey(User,blank=False,null=False, on_delete = models.CASCADE)


class Post(models.Model):
    objects=PostManger()
    question = models.CharField(max_length = 200)
    slug=models.SlugField(blank=True,null=True,unique=True)
    topics = models.ManyToManyField(Topic, blank=False)
    content =RichTextUploadingField(blank=False,null=False, config_name='special')
    image = models.ImageField( upload_to='post',null=False,blank=False)
    tag = TaggableManager()
    author = models.ForeignKey(User,related_name='author',null=False,blank=False, on_delete = models.CASCADE)
    voter=models.ManyToManyField(PostVoter,null=True,blank=True)
    upvote=models.PositiveIntegerField(default=0)
    downvote=models.PositiveIntegerField(default=0)
    total_answer=models.PositiveIntegerField(default=0)
    is_active=models.BooleanField(default=False)
    is_anonymous = models.BooleanField(default=False)
    date_posted = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.question
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.pk},)
    # def save(self,*arg,**kwarg):
    #     # if self.slug is None:
    #     #     self.slug=slugify(self.title)
    #     super().save(*arg,**kwarg)


class Answer(models.Model):
    post = models.ForeignKey(Post, related_name='post_answer', blank=False,null=False,on_delete=models.CASCADE)
    author = models.ForeignKey(User,blank=False,null=False, on_delete = models.CASCADE)
    answer = RichTextUploadingField(blank=False,null=False, config_name='special')
    date_posted = models.DateTimeField(auto_now_add=True)
    upvote=models.PositiveIntegerField(default=0)
    downvote=models.PositiveIntegerField(default=0)
    voter=models.ManyToManyField(PostVoter,null=True,blank=True)
    total_reply=models.PositiveIntegerField(default=0)
    is_anonymous = models.BooleanField(default=False)
    pin_answer = models.BooleanField(default=False)
    class Meta:
        ordering = ['-date_posted']
    def __str__(self):
        return self.answer

class Answer_Reply(models.Model):
    answer= models.ForeignKey(Answer,related_name='reply',blank=False,null=False, on_delete = models.CASCADE)
    author = models.ForeignKey(User, on_delete = models.CASCADE,blank=False,null=False)
    reply = RichTextUploadingField(blank=False,null=False)
    upvote=models.PositiveIntegerField(default=0)
    downvote=models.PositiveIntegerField(default=0)
    date_posted = models.DateTimeField(default=timezone.now)
    voter=models.ManyToManyField(PostVoter,null=True,blank=True)

    class Meta:
        ordering = ['-date_posted']
    def __str__(self):
        return self.reply







# singal 




def slugify_instance(instance,save=False,new_slug=None):
    if new_slug is not None:
        slug=new_slug
    else:
        slug=slugify(instance.question)
    Klass=instance.__class__
    qs=Klass.objects.filter(slug=slug).exclude(id=instance.id)
    print(qs.count())
    if qs.exists():
        slug=f"{slug}-{qs.count()+1}"
        return slugify_instance(instance,save=save,new_slug=slug)
    instance.slug=slug
    if save:
        instance.save()
    return instance

def post_pre_save(sender,instance,*arg,**kwargs):
    if instance.slug is None:
        slugify_instance(instance,save=False)

pre_save.connect(post_pre_save,sender=Post)


# @receiver(post_save, sender=Answer)
# def notification(sender, **kwargs):
#     if kwargs["created"]:
#         """
#         When a user upvotes/downvotes an answer, the answer model is modified as answer's vote_score is updated. This if condition ensures that notifications are only sent when a new answer is created and not everytime when someone upvotes/downvotes the ans
#         """
#         try:
#             from_user = kwargs.get("instance").user
#             to_user = kwargs.get("instance").question.user
#             question = kwargs.get("instance").question
#             is_anonymous = kwargs.get("instance").is_anonymous
#             if is_anonymous:
#                 msg = f"An Anonymous user answered your question: {question}"
#             else:
#                 msg = f"{from_user.first_name} {from_user.last_name} answered your question: {question}"
#             if from_user != to_user:
#                 """Not sending notification in scenarios such as user answering his/her own question"""
#                 Notification.objects.create(
#                     from_user=from_user,
#                     to_user=to_user,
#                     msg=msg,
#                     question=question,
#                     is_anonymous=is_anonymous,
#                     is_answer=True,
#                 )
#             question_followers = FollowQuestion.objects.filter(question=question)
#             if is_anonymous:
#                 # message to the followers of a question
#                 msg = f"An Anonymous user answered a question you were following: {question}"
#             else:
#                 msg = f"{from_user.first_name} {from_user.last_name} answered a question you were following: {question}"
#             for follower in question_followers:
#                 if from_user != follower.user:
#                     """
#                     This ensures that if a user follows a question and then answers that question then he/she
#                     wouldn't get notification
#                     """
#                     Notification.objects.create(
#                         from_user=from_user,
#                         to_user=follower.user,
#                         msg=msg,
#                         question=question,
#                         is_followed_question=True,
#                     )
#         except:
#             from_user = kwargs.get("instance").from_user
#             to_user = kwargs.get("instance").to_user
#             msg = f"{from_user.first_name} {from_user.last_name} started following you"
#             Notification.objects.create(
#                 from_user=from_user, to_user=to_user, msg=msg,
#             )
