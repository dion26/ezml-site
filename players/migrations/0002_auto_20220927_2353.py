# Generated by Django 4.1.1 on 2022-09-27 21:53

from django.db import migrations
from django.core.management import call_command
import os
from pathlib import Path

current_path = Path().absolute()
file_list = []
fixture_folder = os.path.join(current_path, 'players', 'fixtures')
for filename in os.listdir(fixture_folder):
    obj_file = filename.split("_")
    if obj_file[0] == "position" and obj_file[1] == "stp":
        f = os.path.join(fixture_folder, filename)
        # checking if it is a file
        if os.path.isfile(f):
            file_list.append(f)

def add_positions(apps, schema_editor):
    for file_exp in file_list:
        call_command('loaddata', file_exp) 

class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_positions),
    ]