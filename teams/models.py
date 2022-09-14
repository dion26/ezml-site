from django.db import models
from players.models import Player

from django_countries.fields import CountryField
import datetime

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(null=True, default="ezml_logo_opac.svg")
    members = models.ManyToManyField(Player, through='Membership')
    country = CountryField(blank=True, null=True)

    def __str__(self):
        return self.name

class Membership(models.Model):
    STATUS = (
        ('A', 'Active'),
        ('I', 'Inactive'),
        ('L', 'Loan'),
    )
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    date_joined = models.DateField(blank=True, default=datetime.date.today)
    date_left = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS, default='A')