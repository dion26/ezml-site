from django.db.models.signals import post_save
from forums.models import LikeThread, DisLikeThread, Thread


def create_vote(sender, instance, created, **kwargs):
    print('signal triggered')
    if created:
        LikeThread.objects.create(thread=instance)
        DisLikeThread.objects.create(thread=instance)
    else:
        if not hasattr(instance, 'likes'):
            LikeThread.objects.create(thread=instance)
        if not hasattr(instance, 'dis_likes'):
            DisLikeThread.objects.create(thread=instance)

post_save.connect(create_vote, sender=Thread)        