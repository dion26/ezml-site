# Generated by Django 4.1.1 on 2022-10-01 01:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0012_alter_match_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 1, 3, 13, 38, 311340)),
        ),
    ]
