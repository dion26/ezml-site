from django.db import models, IntegrityError
from players.models import Player
from django.utils.text import slugify
import random

from django_countries.fields import CountryField
import datetime

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(null=True, default="ezml_logo_opac.svg")
    members = models.ManyToManyField(Player, through='Membership')
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nickname)
        while True:
            try:
                return super(Team, self).save(*args, **kwargs)
            except IntegrityError:
                r_num = random.randint(0, 100)
                self.slug = slugify(''.join(self.name, str(r_num)))
                return super(Team, self).save(*args, **kwargs)

class Membership(models.Model):
    
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    date_joined = models.DateField(blank=True, default=datetime.date.today)
    date_left = models.DateField(null=True, blank=True)
    