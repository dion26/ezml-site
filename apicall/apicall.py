from mobilelegends_modules import player
from liquipediapy import liquipediapy
from mobilelegends import mobilelegends
import json
import jsondiff as jd
from jsondiff import diff
import time
import os
from urllib.request import urlretrieve
from dateutil.parser import parse as parsedate
import hashlib
import unicodedata
import pycountry
from slugify import slugify

countries = {}
for country in pycountry.countries:
    countries[country.name] = country.alpha_2

liquipy_object = liquipediapy('ezml', 'mobilelegends')
fixture_player_dir = '../players/fixtures/'
fixture_team_dir = '../teams/fixtures/'
# manage.py loaddata <fixturename>
'''
[
  {
    "model": "players.player",
    "pk": 22708183,
    "fields": {"nickname": "Chiilstreeam", 
                "fullname": "Goryachev Andrei", 
                "role": "S", 
                "country": "BY",
                "slug: }
  }, ...
]
'''

# return fixtures: - player_data_fget_stp_02
#                  - team_data_fplayer_stp_06
def push_players():
    ml_obj = mobilelegends('ezml')
    players, teams = ml_obj.get_players()

    with open(f'{fixture_player_dir}player_data_fget_stp_02.json', 'w', encoding='utf-8') as f:
        json.dump(players, f)
    
    with open(f'{fixture_team_dir}team_data_fplayer_stp_06.json', 'w', encoding='utf-8') as f:
        json.dump(teams, f)

# return fixtures: - team_data_fget_04
#                  - player_data_fteam_02_1
def push_teams():
    ml_obj = mobilelegends('ezml')
    teams, players = ml_obj.get_teams()

    with open(f'{fixture_team_dir}team_data_fget_04.json', 'w', encoding='utf-8') as f:
        json.dump(teams, f)
    with open(f'{fixture_player_dir}player_data_fteam_02_1.json', 'w', encoding='utf-8') as f:
        json.dump(players, f)

'''
overrides the format of push players
extend it with more fields

{'info': 
    {'image': 'https://liquipedia.net/commons/images/1/19/Infobox_player_NoImage.png', 
    'name': 'Александр Шарков', 
    'romanized_name': 'Alexander Sharkov', 
    'nationality': '\xa0Russia', 
    'born': 'February 13', 
    'status': 'Active', 
    'roles': 'Jungler', 
    'earnings': 2235}, 
'links': 
    {'instagram': 'https://www.instagram.com/devuoneshot', 
    'tiktok': 'https://tiktok.com/@devuoneshot', 
    'vk': 'https://www.vk.com/klimmoipesik', 
    'youtube': 'https://www.youtube.com/channel/UCHb-orWsq69KfBZbrPKL34Q/featured'}, 
'history': 
    [{'duration': '2020-12-04 — Present', 'name': 'Unique Devu'}], 
    'achivements': [], 
    'gear_settings': {}, 
    'results': []}


 # Additional info for players.player
   [
  {
    "model": "players.player",
    "pk": 22708183,
    "fields": {"image": "player/....png", 
                "born": 'February 13',
                'position': 'Jungler',
                ? "fullname": "Goryachev Andrei",  
                ? "country": "BY"}
  }, ...
] 


# Additional info for membership
[
    {
        model - teams.membership
        pk - same
        fields ->
            "status": "Active"
    }
]


'''

def get_player_info(idx_2_con=1):
    res = []
    player_social = []
    teams_list = []
    temp_team_list_id = []
    member_list = []

    if idx_2_con <= 0:
        idx_2_con = 1

    file_list = []
    static_folder = "../static/images/player/"
    ROLE = {'roamer': "Roamer", 'jungler': "Jungler", "midlaner": "Mid Laner", "explaner": "Exp Laner", "goldlaner": "Gold Laner"}
    SOCIAL = ("youtube", "tiktok", "vk", "facebook")
    STATUS_FIELD = ['Inactive', 'A.', 'Loan', 'C']
    file_index = 1
    
    for filename in os.listdir(fixture_player_dir):
        obj_file = filename.split("_")
        if obj_file[0] == "player" and obj_file[1] == "data":
            f = os.path.join(fixture_player_dir, filename)
            # checking if it is a file
            if os.path.isfile(f):
                file_list.append(f)

    for existing_player in file_list:
        with open(existing_player, 'r') as ext_pl:
            pl_data = json.load(ext_pl)
            ml_obj = mobilelegends('ezml')
            i = 0
            tot = len(pl_data)
            tot_num_iter = 9
            model = "players.player"
            ele_saved_sofar = 0

            for old_player in pl_data:
                player = {}
                social_obj = {}
                
                if file_index < idx_2_con:
                    ##### TODO: use ele so far instead
                    if (i != 0 and i%tot_num_iter == 0) or (pl_data.index(old_player) == tot-1):
                        file_index = file_index + 1
                    i = i+1
                    continue

                player_info = ml_obj.get_player_info(old_player["fields"]["nickname"], results=True)
                
                if not player_info:
                    if (i != 0 and i%tot_num_iter == 0) or (pl_data.index(old_player) == tot-1):
                        file_index = file_index + 1
                    i = i+1
                    continue

                player['model'] = model
                player['pk'] = old_player['pk']
                player['fields'] = {}

                try:
                    logo_name = player_info['info']['image'].split('/')[-1]
                    if 'NoImage' not in logo_name:
                        full_path_logo = ''.join([static_folder, logo_name])
                        urlretrieve(player_info['info']['image'], full_path_logo)
                        player['fields']['image'] = ''.join(['player/', logo_name])
                    else:
                        player['fields']['image'] = ''
                except:
                    player['fields']['image'] = ''
                
                try:
                    player_nat = player_info['info']['nationality']
                    player_nat = countries.get(player_nat, pycountry.countries.search_fuzzy(player_nat)[0].alpha_2)
                    player['fields']['country'] = player_nat
                except LookupError:
                    if 'lao' in player_nat:
                        player['fields']['country'] = 'LA'
                    else:
                        player['fields']['country'] = ''
                except:
                    player['fields']['country'] = ''
                try:
                    status_act = player_info['info']['status']
                    player['fields']['status'] = status_act[0].capitalize()
                except:
                    player['fields']['status'] = ''
                try: # datetime?
                    player_born = player_info['info']['born']
                    player_date = player_born.split("(")[0].strip()
                    player_date = parsedate(player_date)
                    player['fields']['dob'] = player_date.date().isoformat()
                except:
                    player['fields']['dob'] = None

                try:
                    list_player_pos = []
                    player_pos = player_info['info']['roles'].strip().lower().replace(" ", "")
                    for role in ROLE.keys():
                        if role in player_pos:
                            list_player_pos.append(ROLE[role])
                    player['fields']['position'] = list_player_pos
                except:
                    player['fields']['position'] = []

                try:
                    alternate_id = player_info['info']['alternate_ids']
                    player['fields']['alternate_ids'] =  unicodedata.normalize("NFKD", alternate_id).strip()
                except:
                    player['fields']['alternate_ids'] = ''
                
                if not old_player['fields']['fullname']:
                    try:
                        if 'romanized_name' in player_info['info']['name']:
                            name = player_info['info']['romanized_name']
                        else:
                            name = player_info['info']['name']
                        player['fields']['fullname'] = name
                    except:
                        player['fields']['fullname'] = ""

                try:
                    earning = player_info['info']['earnings']
                    player['fields']['earning'] = earning
                except:
                    player['fields']['earning'] = 0

                # SOCIAL
                try:
                    social_obj['pk'] = old_player['pk']
                    social_obj['fields'] = {}
                    social_obj['fields']['owner'] = old_player['pk']
                    for soc in SOCIAL:
                        list_link = [player_info['links'][ele] for ele in player_info['links'].keys()]
                        for link in list_link:
                            if soc in link:
                                social_obj['fields'][soc] = link
                except:
                    social_obj = {}

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

                    member_id = old_player['pk']
                    team_id = int(hashlib.sha256(team.strip().encode('utf-8')).hexdigest(), 16) % 10**8
                    hashstring = team + old_player['fields']['nickname'] + str(duration)
                    member_obj['pk'] = int(hashlib.sha256(hashstring.strip().encode('utf-8')).hexdigest(), 16) % 10**8
                    joined, left = duration.split("—")
                    joined = parsedate(joined.strip()).date().isoformat()
                    try:
                        left = parsedate(left.strip()).date().isoformat()
                    except:
                        left = None
                    member_obj['fields'] = {}
                    member_obj['fields']['player'] = member_id
                    member_obj['fields']['team'] = team_id
                    member_obj['fields']['date_joined'] = joined
                    member_obj['fields']['date_left'] = left
                    if status and status in STATUS_FIELD:
                        member_obj['fields']['status'] = status
                    member_list.append(member_obj)

                    # Team
                    if team_id not in temp_team_list_id:
                        team_obj['pk'] = team_id
                        temp_team_list_id.append(team_id)
                        team_obj['fields'] = {}
                        team_obj['fields']['name'] = team
                        team_obj['fields']['slug'] = slugify(team)
                        teams_list.append(team_obj)

                if social_obj:
                    player_social.append(social_obj)
                res.append(player)

                print(i, "/", tot-1)
                if (i != 0 and i%tot_num_iter == 0) or (pl_data.index(old_player) == tot-1):
                    with open(f'{fixture_player_dir}player_fpinfo_data_{str(file_index)}.json', 'w', encoding='utf-8') as f:
                        json.dump(res, f)
                        res = []
                    with open(f'{fixture_team_dir}member_fpinfo_data_{str(file_index)}.json', 'w', encoding='utf-8') as f:
                        json.dump(member_list, f)
                        member_list = []
                    with open(f'{fixture_team_dir}team_fpinfo_data_{str(file_index)}.json', 'w', encoding='utf-8') as f:
                        json.dump(teams_list, f)
                        teams_list = []
                    with open(f'{fixture_player_dir}social_fpinfo_data_{str(file_index)}.json', 'w', encoding='utf-8') as f:
                        json.dump(player_social, f)
                        player_social = []
                    file_index = file_index + 1
                i = i +1
                
    return res

# ml_obj = mobilelegends('ezml')
# print(ml_obj.get_player_info("chakim"))

# push_players()
# push_teams()
get_player_info(107)