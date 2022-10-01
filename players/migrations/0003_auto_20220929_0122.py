# Generated by Django 4.1.1 on 2022-09-28 23:22

from django.db import migrations
from players.models import Player, Position
from teams.models import Team, Membership

def add_test_players(apps, schema_editor):
    all_position = Position.objects.all()
    number_of_team = 2
    for team in range(number_of_team):
        current_team = Team.objects.create(name=f'team{team}')
        for pos in all_position:
            current_player = Player.objects.create(nickname=f"player_{pos.name}_{team}")
            Membership.objects.create(team=current_team, player=current_player)


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_auto_20220927_2353'),
    ]

    operations = [
        migrations.RunPython(add_test_players)
    ]