# Generated by Django 4.1.1 on 2022-09-20 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0006_auto_20220920_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='status',
            field=models.CharField(choices=[('A', 'Active'), ('R', 'Retired'), ('I', 'Inactive'), ('L', 'Loan')], default='A', max_length=1),
        ),
    ]
