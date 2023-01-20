from django.db import models

# Create your models here.
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)

from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Users should have a Email')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


AUTH_PROVIDERS = {'google': 'google',
                  'email': 'email'}


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    first_name = models.CharField(max_length=255, null=True,blank=True)
    last_name = models.CharField(max_length=255, null=True,blank=True)

    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=255,choices=(('Teacher','Teacher'),('Staf','Staf'),('Student','Student'),('Unknow','Unknow')),default='Staf')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    is_verified=models.BooleanField(default=False)
    token=models.CharField(default='token will  genrated in feature',max_length=500)
    i_answer=models.PositiveIntegerField(default=0)
    i_question=models.PositiveIntegerField(default=0)


    auth_provider = models.CharField(
        max_length=255, blank=False,
        null=False, default=AUTH_PROVIDERS.get('email'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
class Notification(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length = 200)

    content =models.CharField(max_length = 200)
    url_to_open=models.URLField(null=True,blank=True, max_length=200)
    def __str__(self) -> str:
        return self.title