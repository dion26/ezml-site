# Generated by Django 4.1.1 on 2022-10-02 04:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0016_alter_match_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 2, 6, 4, 50, 226800)),
        ),
    ]
