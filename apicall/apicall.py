

from liquipediapy import liquipediapy
from mobilelegends import mobilelegends
import json
from jsondiff import diff
from urllib.request import urlretrieve
from dateutil.parser import parse as parsedate
import hashlib
import unicodedata
import pycountry
from slugify import slugify
from client import Client
import asyncio
from client import Base_Url
from pathlib import Path
import os


countries = {}
for country in pycountry.countries:
    countries[country.name] = country.alpha_2

liquipy_object = liquipediapy('ezml', 'mobilelegends')
fixture_player_dir = '../players/fixtures/'
fixture_team_dir = '../teams/fixtures/'

local_client = Client()

def push_players():
    ml_obj = mobilelegends('ezml')
    players, teams = ml_obj.get_players()
    local_client.create(players, Base_Url.PLAYER)
    local_client.create(teams, Base_Url.TEAM)

def push_teams():
    ml_obj = mobilelegends('ezml')
    teams, players = ml_obj.get_teams()
    new_player_list, ex_player_list = asyncio.run(
                        local_client.sort_objects(players, Base_Url.PLAYER))

    local_client.create(teams, Base_Url.TEAM)
    local_client.create(new_player_list, Base_Url.PLAYER)
    if ex_player_list:
        asyncio.run(local_client.bulk_update(ex_player_list, Base_Url.PLAYER))

def get_players_info(skipped_list=[]):
    new_temp_team_list_id = []
    evaluated_player_id = []

    static_folder = "../static/images/player/"
    ROLE = {'roamer': "Roamer", 'jungler': "Jungler", "midlaner": "Mid Laner", "explaner": "Exp Laner", "goldlaner": "Gold Laner"}
    SOCIAL = ("youtube", "tiktok", "vk", "facebook", "instagram")
    STATUS_FIELD = ['Inactive', 'A.', 'Loan', 'C']

    existing_player = local_client.list_objects(Base_Url.PLAYER)
    total_number = len(existing_player)
    i = 1
    existing_teams = local_client.list_objects(Base_Url.TEAM)
    existing_teams_id = [team['public_id'] for team in existing_teams]

    with open('player_info_evaluated.txt', 'w') as f:
        for old_player in existing_player:
            if old_player['public_id'] in skipped_list:
                continue
            
            ml_obj = mobilelegends('ezml')
            player = {}

            player_info = ml_obj.get_player_info(old_player["nickname"], results=False)
            
            old_logo = old_player['image'].split('/')[-1]
            old_player_nat = old_player['country']
            old_player_stat = old_player['status']
            old_dob = old_player['dob']

            # No Player data detail
            if not player_info:
                continue
            
            player['public_id'] = old_player['public_id']
            player['nickname'] = old_player['nickname']
            # Logo
            try:
                logo_name = player_info['info']['image'].split('/')[-1]
                if 'NoImage' not in logo_name:
                    full_path_logo = ''.join([static_folder, logo_name])
                    player_logo = Path(full_path_logo)
                    logo_path = str(player_logo.resolve())
                    if player_logo.is_file():
                        pass
                    else:
                        logo_path, headers = urlretrieve(player_info['info']['image'], full_path_logo)    
                    if old_logo != logo_name:
                        player['image'] = logo_path
                else:
                    pass
            except:
                pass
            
            # Country
            try:
                player_nat = player_info['info']['nationality']
                player_nat = countries.get(player_nat, pycountry.countries.search_fuzzy(player_nat)[0].alpha_2)
                if player_nat != old_player_nat:
                    player['country'] = player_nat
                else:
                    player['country'] = old_player_nat
            except LookupError:
                player_nat = player_info['info']['nationality']
                if 'lao' in player_nat and 'LA' != old_player_nat:
                    player['country'] = 'LA'
                else:
                    player['country'] = old_player_nat
            except:
                player['country'] = old_player_nat
            
            # status
            try:
                status_act = player_info['info']['status'][0].capitalize()
                if status_act != old_player_stat:
                    player['status'] = status_act
            except:
                pass

            # dob
            try:
                player_born = player_info['info']['born']
                player_date = player_born.split("(")[0].strip()
                player_date = parsedate(player_date)
                if old_dob is not None and parsedate(old_dob) != player_date:
                    player['dob'] = player_date.date().isoformat()
            except:
                pass
            
            # position
            try:
                list_player_pos = []
                player_pos = player_info['info']['roles'].strip().lower().replace(" ", "")
                for role in ROLE.keys():
                    if role in player_pos:
                        list_player_pos.append(ROLE[role])
                player['position'] = list_player_pos
            except:
                pass
            
            # alternate ids
            try:
                alternate_id = player_info['info']['alternate_ids']
                player['alternate_ids'] =  unicodedata.normalize("NFKD", alternate_id).strip()
            except:
                pass
            
            # full name
            if not old_player['fullname']:
                try:
                    if 'romanized_name' in player_info['info']['name']:
                        name = player_info['info']['romanized_name']
                    else:
                        name = player_info['info']['name']
                    player['fullname'] = name
                except:
                    pass
            
            # earning
            try:
                earning = player_info['info']['earnings']
                player['earning'] = earning
            except:
                player['earning'] = 0

            ########## Update Player
            local_client.update(player, old_player['public_id'], Base_Url.PLAYER, old_player['slug'])
            print(f'Update player {old_player["nickname"]}')
            # SOCIAL
            try:
                social_obj = {}
                social_obj['owner'] = old_player['public_id']
                for soc in SOCIAL:
                    list_link = [player_info['links'][ele] for ele in player_info['links'].keys()]
                    for link in list_link:
                        if soc in link:
                            social_obj[soc] = link
                ############ Create Social
                local_client.create(social_obj, Base_Url.SOCIAL)
                print(f'Create Social {old_player["nickname"]}')
            except:
                pass
            
            
            # Member & Teams
            for history in player_info['history']:
                member_obj = {}
                team_obj = {}
                duration = history['duration']
                team = history['name'].split('(')
                if len(team) > 1:
                    status = team[1]
                    team = team[0].strip()
                else:
                    team = team[0].strip()
                    status = None
                # Check if team have (A.)(C.) or other status
                char_to_replace = ['(', ')', ' ']
                if status:
                    for char in char_to_replace:
                        status = status.replace(char, "").strip()
                
                member_id = old_player['public_id']
                team_id = int(hashlib.sha256(team.strip().encode('utf-8')).hexdigest(), 16) % 10**8
                joined, left = duration.split("—")
                joined = parsedate(joined.strip()).date().isoformat()
                try:
                    left = parsedate(left.strip()).date().isoformat()
                except:
                    left = None

                # Team
                if team_id not in existing_teams_id and team_id not in new_temp_team_list_id:
                    team_obj['public_id'] = team_id
                    new_temp_team_list_id.append(team_id)
                    team_obj['name'] = team
                    team_obj['slug'] = slugify(team)
                    ########################## Create Team
                    local_client.create(team_obj, Base_Url.TEAM)
                    print(f'Create Team {team}')

                member_obj['player'] = member_id
                member_obj['team'] = team_id
                member_obj['date_joined'] = joined
                member_obj['date_left'] = left
                if status and status in STATUS_FIELD:
                    member_obj['status'] = status
                ############ Create Membership
                local_client.create(member_obj, Base_Url.MEMBERSHIP)
                print(f'Create Member {old_player["nickname"]}, {team}')

            evaluated_player_id.append(old_player['public_id'])
            f.write(f'{old_player["public_id"]}, ')
            print(f"{i} / {total_number}")
            i = i+1
    return evaluated_player_id

def get_fplayer_achivements():
    ml_obj = mobilelegends('ezml')
    player_info = ml_obj.get_player_info("MobaZane", results=True)
    return player_info

def get_fteam_info():
    ml_obj = mobilelegends('ezml')
    team_info = ml_obj.get_team_info("RRQ Hoshi", results=True)
    return team_info

def get_tours():
    ttype = ['S-Tier', 'A-Tier', 'B-Tier', 'C-Tier', 'D-Tier', 'Monthly', 'Weekly', 'Qualifiers']
    ml_obj = mobilelegends('ezml')
    tournaments = ml_obj.get_tournaments('S-Tier')
    print(tournaments)

# push_players()
# push_teams()
# get_players_info()
# print(get_fplayer_achivements())
# print(get_tours())

data = {
    'public_id': 71568081,
    'nickname' : 'Blink',
    'image' : 'http://127.0.0.1:8000/images/avatar.svg',
    'country' : 'BR'
}

local_client.update(data, 71568081, Base_Url.PLAYER, 'blink')