# Generated by Django 4.1.1 on 2022-09-14 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0003_player_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]