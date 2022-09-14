from mobilelegends_modules import player
from liquipediapy import liquipediapy
from mobilelegends import mobilelegends

liquipy_object = liquipediapy('ezml', 'mobilelegends')
search_result = liquipy_object.search('Wizzking')

ml_obj = mobilelegends('ezml')
players = ml_obj.get_players()

print(players)