from mobilelegends_modules import player
from liquipediapy import liquipediapy
from mobilelegends import mobilelegends
import json

liquipy_object = liquipediapy('ezml', 'mobilelegends')

ml_obj = mobilelegends('ezml')
teams = ml_obj.get_teams()

def push_teams():
    with open('../teams/fixtures/team_data.json', 'w', encoding='utf-8') as f:
            json.dump(teams, f)

# manage.py loaddata <fixturename>
def push_players():
    ml_obj = mobilelegends('ezml')
    players = ml_obj.get_players()

    with open('../players/fixtures/player_data.json', 'w', encoding='utf-8') as f:
        json.dump(players, f)

push_players()

