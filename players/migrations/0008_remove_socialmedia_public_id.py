# Generated by Django 4.1.1 on 2022-10-01 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0007_socialmedia_public_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='socialmedia',
            name='public_id',
        ),
    ]