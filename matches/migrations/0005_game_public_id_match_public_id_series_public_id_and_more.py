# Generated by Django 4.1.1 on 2022-09-29 04:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0004_match_bo_games_match_loser_match_losing_score_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='public_id',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='public_id',
            field=models.PositiveIntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='series',
            name='public_id',
            field=models.PositiveIntegerField(default=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournament',
            name='public_id',
            field=models.PositiveIntegerField(default=4),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='match',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 29, 6, 41, 49, 919640)),
        ),
    ]
