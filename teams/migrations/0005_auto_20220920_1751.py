# Generated by Django 4.1.1 on 2022-09-20 15:51

from django.db import migrations
from django.core.exceptions import ObjectDoesNotExist

import json
import os
from pathlib import Path
# team slug was not made. for future already corrected
from slugify import slugify


current_path = Path().absolute()
file_list = []
fixture_folder = os.path.join(current_path, 'teams', 'fixtures')
for filename in os.listdir(fixture_folder):
    obj_file = filename.split("_")
    if obj_file[0] == "team" and obj_file[1] == "finfo":
        f = os.path.join(fixture_folder, filename)
        # checking if it is a file
        if os.path.isfile(f):
            file_list.append(f)

def add_teams(apps, schema_editor):
    Team = apps.get_model('teams', 'Team')
    for file_exp in file_list:
        file_exp = json.load(open(file_exp, 'r'))
        for data_ele in file_exp:
            insp_pk = data_ele['pk']
            try:
                # Update data: if matched team names are equal
                team_obj_match = Team.objects.get(pk=insp_pk)
                fields_dict = data_ele['fields']
                for key_f in fields_dict.keys():
                    if key_f == 'name':
                        if fields_dict[key_f] != team_obj_match.name:
                            raise Exception('Data with collision of pk')
                        else:
                            continue
                    else:
                        obj_field_value = getattr(team_obj_match, key_f)
                        if fields_dict[key_f]:
                            if fields_dict[key_f] == obj_field_value:
                                continue
                            else:
                                # Replacing the database
                                # Position field is a list
                                # Many2m rel resolve with set
                                setattr(team_obj_match, key_f, fields_dict[key_f])
                team_obj_match.save()
            except ObjectDoesNotExist:
                # New Team found create new team
                Team.objects.create(pk=insp_pk, name=data_ele['fields']["name"], slug=slugify(data_ele['fields']['name']))

class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0004_remove_membership_status'),
        ('players', '0012_auto_20220920_1557'),
    ]

    operations = [
        migrations.RunPython(add_teams),
    ]