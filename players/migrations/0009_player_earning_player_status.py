# Generated by Django 4.1.1 on 2022-09-20 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0008_player_alternate_ids_player_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='earning',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='status',
            field=models.CharField(choices=[('A', 'Active'), ('R', 'Retired'), ('I', 'Inactive'), ('L', 'Loan')], default='A', max_length=1),
        ),
    ]