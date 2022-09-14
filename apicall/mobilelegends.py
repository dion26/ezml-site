from msilib.schema import tables
import exceptions as ex
from liquipediapy import liquipediapy
import re
import unicodedata
from mobilelegends_modules.player import ml_player
from mobilelegends_modules.team import ml_team
import itertools
from urllib.request import quote
import time

class mobilelegends():
    def __init__(self,appname):
        self.appname = appname
        self.liquipedia = liquipediapy(appname,'mobilelegends')
        self.__image_base_url = 'https://liquipedia.net'

    def get_players(self):
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
                            player['id'] = cols[0]
                            player['name'] = cols[1]
                            player['role'] = cols[2]
                            player['country'] = country
                            player['team'] = team
                            players.append(player)
            index_now = regions.index(region)
            print("get_players: ", index_now + 1, "/", total_region, ", Region: ", region, " is parsed")
            if (index_now < total_region - 1):
                time.sleep(31)
        return players

    def get_teams(self,regions=[]):
        if not regions:
            regions = ['South_America', 'Southeast_Asia']
        
        if isinstance(regions, str):
            regions = [regions]

        teams = []
        total_region = len(regions)

        for region in regions:
            soup,__ = self.liquipedia.parse('Portal:Teams/'+region)
            tables = soup.find_all('table',class_='collapsible')
            for table in tables:
                team = {}
                table_body = table.find('tbody')
                rows = table_body.find_all('tr')
                head = rows[0]
                team_name = head.find('span',class_='team-template-text').get_text()
                team_logo = self.__image_base_url+head.find('span',class_='team-template-team-standard').find('img').get('src')
                team['name'] = team_name
                team['logo'] = team_logo
                team['players'] = []
                for row in rows[2:]:
                    player = {}
                    cols = row.find_all('td')
                    links = cols[0].find_all('a')
                    player_country = links[0].get('title')
                    cols = [ele.text.strip() for ele in cols]
                    # teams.append([ele for ele in cols if ele])
                    player['id'] = cols[0]
                    player['name'] = cols[1]
                    player['country'] = player_country
                    team['players'].append(player)
                teams.append(team)

            index_now = regions.index(region)
            print("get_teams: ", index_now + 1, "/", total_region, ", Region: ", region, " is parsed")
            if (index_now < total_region - 1):
                time.sleep(31)
        return teams