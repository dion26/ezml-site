from django.db import models
from django_countries.fields import CountryField

# Create your models here.
class Player(models.Model):
    ROLE = (
        ('P', 'Player'),
        ('A', 'Analyst'),
        ('C', 'Coach'),
        ('S', 'Caster'),
    )
    nickname = models.CharField(max_length=60)
    fullname = models.CharField(max_length=60, blank=True, null=True)
    country = CountryField(blank=True, null=True)
    role = models.CharField(max_length=1, choices=ROLE, default='P')
    # team =
    # past teams =
    # Heros
    # Match history
    # links twitch/twitter/youtube
    # form history (hltv)
    def __str__(self):
        return self.nickname

