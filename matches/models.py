from asyncio import staggered
from datetime import datetime
from email.policy import default
import datetime
from unittest import result
from unittest.util import _MAX_LENGTH
from django.db import models
from django_countries.fields import CountryField
from djmoney.models.fields import MoneyField
from django.core.exceptions import ValidationError

from teams.models import Team

# Create your models here.
class Series(models.Model):
    public_id = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Tournament(models.Model):
    public_id = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=200)
    series = models.ForeignKey(Series, on_delete=models.SET_NULL, null=True, blank=True)
    country = CountryField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    prize = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', blank=True, default=0)
    participants = models.ManyToManyField(Team, through='Participation')

    def __str__(self):
        return self.name

class Participation(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name="has_participant")
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="participate_in")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['tournament', 'team'], name='unique event')
        ]

    def __str__(self):
        return f'{self.team.name} in {self.tournament.name}'

class Match(models.Model):
    public_id = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=250, default="")
    teams = models.ManyToManyField(Participation, related_name='have_matches')
    bo_games = models.PositiveSmallIntegerField(default=3)
    winner = models.ForeignKey(Participation, on_delete=models.CASCADE, blank=True, null=True, related_name="won_in_match")
    loser = models.ForeignKey(Participation, on_delete=models.CASCADE, blank=True, null=True, related_name="lost_in_match")
    winning_score = models.PositiveSmallIntegerField(default=0)
    losing_score = models.PositiveSmallIntegerField(default=0)
    start = models.DateTimeField(default=datetime.datetime.now())

class Game(models.Model):
    public_id = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=250, default="")
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    blue_team = models.ForeignKey(Participation, on_delete=models.CASCADE, blank=True, null=True, related_name="as_blue")
    red_team = models.ForeignKey(Participation, on_delete=models.CASCADE, blank=True, null=True, related_name="as_red")
    winner = models.ForeignKey(Participation, on_delete=models.CASCADE, blank=True, null=True, related_name="won_game")
    loser = models.ForeignKey(Participation, on_delete=models.CASCADE, blank=True, null=True, related_name="lost_game")
    winning_score = models.PositiveSmallIntegerField(default=0)
    losing_score = models.PositiveSmallIntegerField(default=0)
    duration = models.DurationField()