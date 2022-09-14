from msilib.schema import tables
import exceptions as ex
from liquipediapy import liquipediapy
import re
import unicodedata
from mobilelegends_modules.player import ml_player
from mobilelegends_modules.team import ml_team
import itertools
from urllib.request import quote, urlretrieve
import time

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
        pk = 1
        regions = ['Europe', 'CIS', 'North_America','South_America', 'South_Asia', 'Southeast_Asia', 'East_Asia', 'Middle_East_Africa']
        players = []
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
                            players.append(player)
                            pk = pk+1
            index_now = regions.index(region)
            print("get_players: ", index_now + 1, "/", total_region, ", Region: ", region, " is parsed")
            if (index_now < total_region - 1):
                time.sleep(31)
        return players

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
        pk = 1

        for region in regions:
            soup,__ = self.liquipedia.parse('Portal:Teams/'+region)
            tables = soup.find_all('table',class_='collapsible')
            for table in tables:
                team = {}
                team['model'] = model
                team['pk'] = pk
                team['fields'] = {}
                table_body = table.find('tbody')
                rows = table_body.find_all('tr')
                head = rows[0]
                team_name = head.find('span',class_='team-template-text').get_text()
                team_logo = self.__image_base_url+head.find('span',class_='team-template-team-standard').find('img').get('src')
                team['fields']['name'] = team_name
                logo_name = team_logo.split('/')[-1]
                static_folder = "../static/images/team/"
                full_path_logo = ''.join([static_folder, logo_name])
                urlretrieve(team_logo, full_path_logo)
                team['fields']['logo'] = ''.join(['team/', logo_name])
                # team['players'] = []
                # for row in rows[2:]:
                #     player = {}
                #     cols = row.find_all('td')
                #     links = cols[0].find_all('a')
                #     player_country = links[0].get('title')
                #     cols = [ele.text.strip() for ele in cols]
                #     # teams.append([ele for ele in cols if ele])
                #     player['id'] = cols[0]
                #     player['name'] = cols[1]
                #     player['country'] = player_country
                #     team['players'].append(player)
                teams.append(team)
                pk=pk+1

            index_now = regions.index(region)
            print("get_teams: ", index_now + 1, "/", total_region, ", Region: ", region, " is parsed")
            if (index_now < total_region - 1):
                time.sleep(31)
        return teams