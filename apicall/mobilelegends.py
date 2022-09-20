from msilib.schema import tables
import exceptions as ex
from liquipediapy import liquipediapy
import re

from mobilelegends_modules.player import ml_player
from mobilelegends_modules.team import ml_team
import itertools
from urllib.request import quote, urlretrieve
import time
import hashlib
from slugify import slugify

import pycountry

countries = {}
for country in pycountry.countries:
    countries[country.name] = country.alpha_2

class mobilelegends():
    def __init__(self,appname):
        self.appname = appname
        self.liquipedia = liquipediapy(appname,'mobilelegends')
        self.__image_base_url = 'https://liquipedia.net'

    def get_players(self):
        model = 'players.player'
        regions = ['Europe', 'CIS', 'North_America','South_America', 'South_Asia', 'Southeast_Asia', 'East_Asia', 'Middle_East_Africa']
        players = []
        model_team = 'teams.team'
        teams = []
        team_ids = []
        total_region = len(regions)
        for region in regions:			
            soup,__ = self.liquipedia.parse('Portal:Players/'+quote(region))
            tables = soup.find_all('table', attrs={'class': 'wikitable'})
            for table in tables:
                table_bodies = table.find_all('tbody')
                for table_body in table_bodies:
                    rows = table_body.find_all('tr')
                    for row in rows:
                        player = {}
                        team_obj = {}
                        cols = row.find_all('td')
                        cols = [ele.text.strip() for ele in cols]
                        if cols:
                            try:
                                country = row.find('a').get('title')
                            except AttributeError:
                                country = ''
                            try:
                                team = row.find('span',class_='team-template-image-icon').find('a').get('title')
                            except AttributeError:
                                team = ''
                            if team and team not in team_ids:
                                pk_team = int(hashlib.sha256(team.encode('utf-8')).hexdigest(), 16) % 10**8
                                team_obj['model'] = model_team
                                team_obj['pk'] = pk_team
                                team_obj['fields'] = {}
                                team_obj['fields']['name'] = team
                                team_obj['fields']['slug'] = slugify(team)
                                team_ids.append(team)
                                teams.append(team_obj)
                            pk = int(hashlib.sha256(cols[0].encode('utf-8')).hexdigest(), 16) % 10**8
                            player['model'] = model
                            player['pk'] = pk
                            player['fields'] = {}
                            player['fields']['nickname'] = cols[0]
                            player['fields']['fullname'] = cols[1]
                            role = cols[2]
                            if 'coach' in role.lower():
                                player['fields']['role'] = 'C'
                            elif 'analyst' in role.lower():
                                player['fields']['role'] = 'A'
                            elif 'caster' in role.lower():
                                player['fields']['role'] = 'S'
                            else:
                                player['fields']['role'] = 'P'
                            try:
                                player['fields']['country'] = countries.get(country, pycountry.countries.search_fuzzy(country)[0].alpha_2)
                            except LookupError:
                                if 'lao' in country:
                                    player['fields']['country'] = 'LA'
                                else:
                                    player['fields']['country'] = ''
                            player['fields']['slug'] = slugify(cols[0])
                            players.append(player)

            index_now = regions.index(region)
            print("get_players: ", index_now + 1, "/", total_region, ", Region: ", region, " is parsed")
            if (index_now < total_region - 1):
                time.sleep(31)
        return [players, teams]

    # def update_player
    # For new data, pk can be different 
    # any update from source should care about tbis

    def get_teams(self,regions=[]):
        if not regions:
            regions = ['South_America', 'Southeast_Asia']
        
        if isinstance(regions, str):
            regions = [regions]

        teams = []
        total_region = len(regions)
        model = 'teams.team'
        player_id = []
        players = []

        for region in regions:
            soup,__ = self.liquipedia.parse('Portal:Teams/'+region)
            tables = soup.find_all('table',class_='collapsible')
            for table in tables:
                team = {}
                team['model'] = model
                table_body = table.find('tbody')
                rows = table_body.find_all('tr')
                head = rows[0]
                team_name = head.find('span',class_='team-template-text').get_text()
                team['pk'] = int(hashlib.sha256(team_name.encode('utf-8')).hexdigest(), 16) % 10**8
                team['fields'] = {}
                team_logo = self.__image_base_url+head.find('span',class_='team-template-team-standard').find('img').get('src')
                team['fields']['name'] = team_name
                team['fields']['slug'] = slugify(team_name)
                logo_name = team_logo.split('/')[-1]
                static_folder = "../static/images/team/"
                full_path_logo = ''.join([static_folder, logo_name])
                urlretrieve(team_logo, full_path_logo)
                team['fields']['logo'] = ''.join(['team/', logo_name])
                
                model_player = 'players.player'
                for row in rows[2:]:
                    player = {}
                    cols = row.find_all('td')
                    links = cols[0].find_all('a')
                    player_country = links[0].get('title')
                    try:
                        cols = [ele.text.strip() for ele in cols]
                    except:
                        cols = []
                    # teams.append([ele for ele in cols if ele])
                    if cols and cols[0] not in player_id:
                        player['model'] = model_player
                        player['pk'] = int(hashlib.sha256(cols[0].encode('utf-8')).hexdigest(), 16) % 10**8
                        player['fields'] = {}
                        player['fields']['nickname'] = cols[0]
                        player['fields']['fullname']  = cols[1]
                        player['fields']['slug']  = slugify(cols[0])
                        try:
                            player['fields']['country'] = countries.get(player_country, pycountry.countries.search_fuzzy(player_country)[0].alpha_2)
                        except LookupError:
                            if 'lao' in player_country:
                                player['fields']['country'] = 'LA'
                            else:
                                player['fields']['country'] = ''
                        players.append(player)
                        player_id.append(cols[0])
                teams.append(team)

            index_now = regions.index(region)
            print("get_teams: ", index_now + 1, "/", total_region, ", Region: ", region, " is parsed")
            if (index_now < total_region - 1):
                time.sleep(31)
        return [teams, players]

    def get_player_info(self,playerName,results=False):
        player_object = ml_player()
        playerName = player_object.process_playerName(playerName)		
        soup,redirect_value = self.liquipedia.parse(playerName)
        if redirect_value is not None:
            playerName = redirect_value
        player = {}
        player['info'] = player_object.get_player_infobox(soup)
        player['links'] = player_object.get_player_links(soup)
        player['history'] = player_object.get_player_history(soup)
        player['achivements'] = player_object.get_player_achivements(soup)

        if results:
            parse_value = playerName + "/Results"
            time.sleep(31)
            try:
                soup,__ = self.liquipedia.parse(parse_value)
            except ex.RequestsException:
                player['results'] = []
            else:	
                player['results'] = player_object.get_player_achivements(soup)

        return player