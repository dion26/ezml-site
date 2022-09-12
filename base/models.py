from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser

from django.core.cache import cache 
import datetime
from ezml_site import settings

class User(AbstractUser):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)

    avatar = models.ImageField(null=True, default="avatar.svg")

    def last_seen(self):
        return cache.get('seen_%s' % self.username)

    def online(self):
        if self.last_seen():
            now = datetime.datetime.now()
            if now > self.last_seen() + datetime.timedelta(
                        seconds=settings.USER_ONLINE_TIMEOUT):
                return False
            else:
                return True
        else:
            return False 

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']