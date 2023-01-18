from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User,related_name='profile', on_delete = models.CASCADE)
    type = models.CharField(max_length=255,choices=(('Teacher','Teacher'),('Staf','Staf'),('Student','Student'),('Unknow','Unknow')),default='Staf')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    is_verified=models.BooleanField(default=False)
    token=models.CharField(default='token will  genrated in feature',max_length=500)
    i_answer=models.PositiveIntegerField(default=0)
    i_question=models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 and img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    def __str__(self) -> str:
        return self.user.username
class Notification(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length = 200)

    content =models.CharField(max_length = 200)
    url_to_open=models.URLField(null=True,blank=True, max_length=200)
    def __str__(self) -> str:
        return self.title



    