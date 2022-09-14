# Generated by Django 4.1.1 on 2022-09-14 02:05

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=100)),
                ('fullname', models.CharField(blank=True, max_length=100, null=True)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
            ],
        ),
    ]
