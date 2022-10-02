import exceptions as ex
from liquipediapy import liquipediapy
from mobilelegends_modules.player import ml_player
from mobilelegends_modules.team import ml_team
from urllib.request import quote, urlretrieve
import time
import hashlib
from slugify import slugify
import pycountry
import unicodedata
import asyncio
from pathlib import Path

countries = {}
for country in pycountry.countries:
    countries[country.name] = country.alpha_2

class mobilelegends():
    def __init__(self,appname):
        self.appname = appname
        self.liquipedia = liquipediapy(appname,'mobilelegends')
        self.__image_base_url = 'https://liquipedia.net'

        # init for get teams

    def get_players(self):
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
                                team_obj['public_id'] = pk_team
                                team_obj['name'] = team
                                team_obj['slug'] = slugify(team)
                                team_ids.append(team)
                                teams.append(team_obj)
                            pk = int(hashlib.sha256(cols[0].encode('utf-8')).hexdigest(), 16) % 10**8
                            player['public_id'] = pk
                            player['nickname'] = cols[0]
                            player['fullname'] = cols[1]
                            role = cols[2]
                            if 'coach' in role.lower():
                                player['role'] = 'C'
                            elif 'analyst' in role.lower():
                                player['role'] = 'A'
                            elif 'caster' in role.lower():
                                player['role'] = 'S'
                            else:
                                player['role'] = 'P'

                            try:
                                player['country'] = countries.get(country, pycountry.countries.search_fuzzy(country)[0].alpha_2)
                            except LookupError:
                                if 'lao' in country:
                                    player['country'] = 'LA'
                                else:
                                    player['country'] = ''
                            player['slug'] = slugify(cols[0])
                            players.append(player)

            index_now = regions.index(region)
            print("get_players: ", index_now + 1, "/", total_region, ", Region: ", region, " is parsed")
            if (index_now < total_region - 1):
                time.sleep(31)
        return [players, teams]

    # def update_player
    # For new data, pk can be different 
    # any update from source should care about tbis

    async def get_data_tables(self, tables):
        player_id = []
        teams = []
        players = []
        for table in tables:
            team = {}
            table_body = table.find('tbody')
            rows = table_body.find_all('tr')
            head = rows[0]
            team_name = head.find('span',class_='team-template-text').get_text()
            team['public_id'] = int(hashlib.sha256(team_name.encode('utf-8')).hexdigest(), 16) % 10**8
            team['fields'] = {}
            team_logo = self.__image_base_url+head.find('span',class_='team-template-team-standard').find('img').get('src')
            team['name'] = team_name
            team['slug'] = slugify(team_name)
            logo_name = team_logo.split('/')[-1]
            static_folder = "../static/images/team/"
            full_path_logo = ''.join([static_folder, logo_name])
            pic_file = Path(full_path_logo)

            # check for duplicate
            if pic_file.is_file():
                pass
            else:
                try:
                    urlretrieve(team_logo, full_path_logo)
                except:
                    print(f'data {team_logo} can not be opened')
    
            team['logo'] = ''.join(['team/', logo_name])
            
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
                    player['public_id'] = int(hashlib.sha256(cols[0].encode('utf-8')).hexdigest(), 16) % 10**8
                    player['nickname'] = cols[0]
                    player['fullname']  = cols[1]
                    player['slug']  = slugify(cols[0])
                    try:
                        player['country'] = countries.get(player_country, pycountry.countries.search_fuzzy(player_country)[0].alpha_2)
                    except LookupError:
                        if 'lao' in player_country:
                            player['country'] = 'LA'
                        else:
                            player['country'] = ''
                    players.append(player)
                    player_id.append(cols[0])
            teams.append(team)
        return (teams, players)

    def get_teams(self,regions=[]):
        if not regions:
            regions = ['South_America', 'Southeast_Asia']
        
        if isinstance(regions, str):
            regions = [regions]

        total_region = len(regions)
        for region in regions:
            soup,__ = self.liquipedia.parse('Portal:Teams/'+region)
            tables = soup.find_all('table',class_='collapsible')
            teams, players = asyncio.run(self.get_data_tables(tables))

            index_now = regions.index(region)
            print("get_teams: ", index_now + 1, "/", total_region, ", Region: ", region, " is parsed")
            if (index_now < total_region - 1):
                time.sleep(31)
        return [teams, players]

    def get_player_info(self,playerName, results=False):
        player_object = ml_player()
        playerName = player_object.process_playerName(playerName)
        
        time.sleep(31)
        try:	
            soup,redirect_value = self.liquipedia.parse(playerName)
        except ex.RequestsException:
            player = {}
            return player
        
        if redirect_value is not None:
            playerName = redirect_value
        player = {}
        player['info'] = player_object.get_player_infobox(soup)
        player['links'] = player_object.get_player_links(soup)
        player['history'] = player_object.get_player_history(soup)
        # player['achivements'] = player_object.get_player_achivements(soup)

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

    def get_team_info(self,teamName,results=True,play_h=True):
        team_object = ml_team()
        teamName = team_object.process_teamName(teamName)	
        soup,redirect_value = self.liquipedia.parse(teamName)
        time.sleep(31)
        if redirect_value is not None:
            teamName = redirect_value
        team = {}
        team['info'] = team_object.get_team_infobox(soup)	
        team['links'] = team_object.get_team_links(soup)
        team['team_roster'] = team_object.get_team_roster(soup)
        # team['achivements'] = team_object.get_team_achivements(soup)
        if results:
            parse_value = teamName + "/Results"
            try:
                soup,__ = self.liquipedia.parse(parse_value)
            except ex.RequestsException:
                team['results'] = []
            else:	
                team['results'] = team_object.get_team_achivements(soup)
            time.sleep(31)
        if play_h:
            parse_value = teamName + '/Played_Matches'
            try:
                soup,__ = self.liquipedia.parse(parse_value)
            except ex.RequestsException:
                team['play_h'] = []
            else:	
                team['play_h'] = team_object.get_played_match(soup)
            time.sleep(31)
        return team

    # test
    def get_transfers(self):
        transfers = []
        soup,__ = self.liquipedia.parse('Portal:Transfers')
        index_values = []
        header_row = soup.find('div',class_='divHeaderRow')
        cells = header_row.find_all('div',class_='divCell')
        for cell in cells:
            index_values.append(cell.get_text().strip())
        rows = soup.find_all('div',class_='divRow')	
        for row in rows:
            transfer = {}
            cells = row.find_all('div',class_='divCell')
            for i in range(0,len(cells)):
                key = index_values[i]
                value = cells[i].get_text()
                if key == "Player":
                    value = [val for val in value.split(' ') if len(val) > 0]
                if key == "Old" or key == "New":
                    try:
                        value = cells[i].find('a').get('title')	
                    except	AttributeError:
                        value = "None"
                transfer[key] = value
            transfer = {k: v for k, v in transfer.items() if len(k) > 0}	
            transfers.append(transfer)	

        return transfers
    
    # test
    def get_upcoming_and_ongoing_games(self):
        games = []
        soup,__ = self.liquipedia.parse('Liquipedia:Matches')
        matches = soup.find_all('table',class_='infobox_matches_content')
        for match in matches:
            game = {}
            cells = match.find_all('td')
            try:
                game['team1'] = cells[0].find('span',class_='team-template-image').find('a').get('title')			
                game['team2'] = cells[2].find('span',class_='team-template-image').find('a').get('title')
                game['start_time'] = cells[3].find('span',class_="timer-object").get_text()
                game['tournament'] = cells[3].find('div').get_text().rstrip()
                try:
                    game['twitch_channel'] = cells[3].find('span',class_="timer-object").get('data-stream-twitch')
                except AttributeError:
                    pass
                games.append(game)	
            except AttributeError:
                continue		
                    
        return games


    def get_tournaments(self,tournamentType=None):
        tournaments = []
        if tournamentType is None:
            page_val = 'Portal:Tournaments'
        else:
            page_val = tournamentType+'_Tournaments'
        print(page_val)
        time.sleep(31)				
        soup,__ = self.liquipedia.parse(page_val)
        tables = soup.find_all('div',class_='divTable')
        for table in tables:
            rows = table.find_all('div',class_='divRow')
            for row in rows:
                tournament = {}
                tournament_cell = row.find('div',class_='Tournament')
                tournament['series'] = tournament_cell.find('a')['title']
                tournament['tournament'] = tournament_cell.find('b').get_text()
                tournament['date'] = row.find('div',class_='EventDetails-Left-55').get_text()
                tournament['prize'] = unicodedata.normalize("NFKD",row.find('div',class_='EventDetails-Right-45').get_text().rstrip())
                team_no = unicodedata.normalize("NFKD",row.find('div',class_='EventDetails-Right-40').get_text().rstrip()).split()
                tournament['teams_no'] = team_no[0]
                location = unicodedata.normalize("NFKD",row.find('div',class_='EventDetails-Left-60').get_text().rstrip()).split(',')
                try:
                    tournament['host_locaion'] = location[1]
                except IndexError:	
                    tournament['host_locaion'] = ''	
                tournament['event_locaion'] = location[0]

                placement = row.find_all('div',class_='Placement')
                if len(placement) > 1:
                    try:
                        tournament['first_place'] = row.find('div',class_='FirstPlace').find('span',class_='team-template-text').find('a')['title']	
                    except AttributeError:	
                        tournament['first_place'] = 'TBD'

                    try:
                        tournament['second_place'] = row.find('div',class_='SecondPlace').find('span',class_='team-template-text').find('a')['title']		
                    except AttributeError:	
                        tournament['second_place'] = 'TBD'
                else:
                    teams = row.find('div',class_='Placement').find_all('span',class_='Player')
                    qual_teams = []
                    for team in teams:
                        qual_teams.append(team.find('span',class_='team-template-text').get_text())
                    
                    tournament['qualified'] = qual_teams
                        
                tournaments.append(tournament)

        return tournaments

    # test
    def get_heros(self):
        soup,__ = self.liquipedia.parse('Portal:Heroes')
        heros = []
        page_list = soup.find_all('li')
        for item in page_list:
            hero = {}
            try:
                hero['image'] = self.__image_base_url + item.find('img').get('src')
            except AttributeError:
                continue	
            hero['name'] = item.get_text()
            heros.append(hero)
        return heros

    # test
    def get_hero_info(self,heroName):
        hero = {}
        heroName = heroName.replace(' ','_')
        soup,__ = self.liquipedia.parse(heroName)	
        try:
            image_url = soup.find('div', class_='infobox-image').find('img').get('src')		
            if 'PlayerImagePlaceholder' not in image_url:
                hero['image'] = self.__image_base_url+image_url
            else:
                hero['image'] = ''	
        except AttributeError:
            hero['image'] = ''		
        info_boxes = soup.find_all('div', class_='infobox-cell-2')
        for i in range(0,len(info_boxes),2):
            attribute = info_boxes[i].get_text().replace(':','')
            if attribute == "Side":
                hero['side'] =  info_boxes[i+1].get_text().rstrip().split(',')
            else:	
                attribute = attribute.lower().replace('(', '').replace(')', '').replace(' ','_')
                hero[attribute] = info_boxes[i+1].get_text().rstrip()

        return hero
    
    # get equipments Portal:Equipment
    # get equipment info
    # get emblems
    # get battle spell
    # get battle spell info

    