from django.db import models
from django_countries.fields import CountryField

# Create your models here.
class Player(models.Model):
    nickname = models.CharField(max_length=100)
    fullname = models.CharField(max_length=100, blank=True, null=True)
    country = CountryField(blank=True, null=True)
    # team =
    # past teams =
    # Heros
    # Match history
    # links twitch/twitter/youtube
    # form history (hltv)
    
