# Generated by Django 4.1.1 on 2022-09-19 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0007_alter_player_positions'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='alternate_ids',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]
