# Generated by Django 4.1.1 on 2022-09-30 14:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0009_alter_match_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 30, 16, 8, 47, 717886)),
        ),
    ]
