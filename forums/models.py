from django.db import models
from django.contrib import admin

from base.models import User

from ckeditor.fields import RichTextField
import datetime
import pytz
import math

class Subforum(models.Model):
    name = models.CharField(max_length=200)

    def url_argument(self):
        return '-'.join(self.name.lower().split())

    def __str__(self):
        return self.name

class Thread(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    subforum = models.ForeignKey(Subforum, on_delete=models.SET_NULL, null=True)
    sticked = models.BooleanField(default=False)
    # image

    name = models.CharField(max_length=200)
    description = models.CharField(null=True, blank=True, max_length=200)
    text_fill = RichTextField(null=True, blank=True,)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def get_total_likes(self):
        try:
            likes = self.likes.users.count()
        except:
            likes = 0
        return likes
    
    def get_total_dis_likes(self):
        try:
            dlikes = self.dis_likes.users.count()
        except:
            dlikes = 0
        return dlikes

    def get_hot_score(self):
        score = math.log(abs(self.get_total_likes() - self.get_total_dis_likes() + 0.5))
        utc = pytz.utc
        now = datetime.datetime.utcnow().replace(tzinfo=utc)
        weight = (now - self.created).total_seconds()/45000
        return score/weight

    def get_top_score(self):
        score = self.get_total_likes() - self.get_total_dis_likes()
        return score

    def __str__(self):
        return str(self.name)

class LikeThread(models.Model):

    thread = models.OneToOneField(Thread, related_name="likes", on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='requirement_thread_likes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @admin.display(description='count')
    def get_total_likes(self):
        try:
            likes = self.users.count()
        except:
            likes = 0
        return likes

    def __str__(self):
        return str(self.thread.name)[:30]

class DisLikeThread(models.Model):

    thread = models.OneToOneField(Thread, related_name="dis_likes", on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='requirement_thread_dis_likes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @admin.display(description='count')
    def get_total_dis_likes(self):
        try:
            dlikes = self.users.count()
        except:
            dlikes = 0
        return dlikes

    def __str__(self):
        return str(self.thread.name)[:30]

class FavoriteThread(models.Model):

    thread = models.OneToOneField(Thread, related_name="fav_thread", on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='requirement_thread_fav')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.thread.name)[:30]

class Comment(models.Model):
    # likes
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def get_total_likes(self):
        return self.likes.users.count()

    def get_total_dis_likes(self):
        return self.dis_likes.users.count()

    def __str__(self):
        return self.body[0:50]

class LikeComment(models.Model):
    ''' like  comment '''

    comment = models.OneToOneField(Comment, related_name="likes", on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='requirement_comment_likes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.comment.comment)[:30]

class DisLikeComment(models.Model):
    ''' Dislike  comment '''

    comment = models.OneToOneField(Comment, related_name="dis_likes", on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='requirement_comment_dis_likes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.comment.comment)[:30]