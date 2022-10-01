from urllib.request import quote
import re
import itertools
import unicodedata
from urllib.request import urlretrieve
import pycountry
import pandas as pd

countries = {}
for country in pycountry.countries:
    countries[country.name] = country.alpha_2

class ml_team():
	def __init__(self):
		self.__image_base_url = 'https://liquipedia.net'
		self.__image_local_base_url = "../static/images/team/"

	def process_teamName(self,teamName):
		teamName = teamName.replace(" ","_")
		teamName = quote(teamName)

		return teamName

	def get_ISO_country_code(self, country):
		try:
			code_nat = countries.get(country, pycountry.countries.search_fuzzy(country)[0].alpha_2)
		except LookupError:
			if 'lao' in country:
				code_nat = 'LA'
			else:
				code_nat = ''
		return code_nat

	def get_team_infobox(self,soup):
		team = {}
		try:
			image_url = soup.find('div', class_='infobox-image').find('img').get('src')	
			logolink = self.__image_base_url+image_url
			logoname = image_url.split('/')[-1]
			full_path_logo = ''.join([self.__image_local_base_url, logoname])
			urlretrieve(logolink, full_path_logo)
			team['image'] = full_path_logo
		except AttributeError:
			team['image'] = ''			
		info_boxes = soup.find_all('div', class_='infobox-cell-2')
		for i in range(0,len(info_boxes),2):
			attribute = info_boxes[i].get_text().replace(':','')
			if attribute == "Sponsor" or attribute == "Location":
				value_list = []
				values = info_boxes[i+1].find_all('a')
				for value in values:
					text = value.get_text()
					if len(text) > 0:
						if attribute == 'Location':
							value_list.append(self.get_ISO_country_code(text))
						else:
							value_list.append(text)
				team[attribute.lower()] = value_list
			elif attribute == "Total Earnings":
				team['earnings'] = int(info_boxes[i+1].get_text().replace('$','').replace(',',''))
			elif attribute == "Games":
				games = []
				game_values = info_boxes[i+1].find_all('i')	
				for game in game_values:
					games.append(game.get_text())
				team['games'] = games			
			else:
				team[attribute.lower().strip()] = unicodedata.normalize("NFKD",info_boxes[i+1].get_text()).strip()
		return team	

	def get_team_links(self,soup):
		team_links = {}
		try:		
			links = soup.find('div', class_='infobox-icons').find_all('a')
		except AttributeError:
			return team_links
		for link in links:
			link_list = link.get('href').split('.')
			site_name = link_list[-2].replace('https://','')
			team_links[site_name] = link.get('href')

		return team_links	


	def get_team_roster(self,soup):
		roster = soup.find_all(
			"table",class_="wikitable wikitable-striped roster-card"
		)
		roster = [obj.find("tbody") for obj in roster]
		players_dict = {}
		for roster_tab in roster:
			title = roster_tab.tr.th.text
			rows = roster_tab.find_all("tr")
			if title not in players_dict.keys():
				players_dict[title] = []
			for tag in rows:
				player = {}
				try:
					player["Country"] = tag.find("span", class_="flag").a["title"]
				except AttributeError:
					pass

				try:
					player["ID"] = (
						tag.find(
							"span", attrs={"style": "white-space:pre"}
						).a.text
					)
				except AttributeError:
					try:
						player["ID"] = (
							tag.find(
								"td", class_="ID"
							)
							.get_text()
							.strip()
						)
					except:
						pass
					pass
				special_chars = '()'
				try:
					player["Name"] = (
						tag.find(
							"td", class_="Name"
						).get_text()
						.strip()
					)
					for char in special_chars:
						player["Name"] = player["Name"].replace(char, '')
				except AttributeError:
					pass
				
				try:
					player["Position"] = (
						tag.find(
							"td", class_="Position"
						).get_text()
						.split(':')[1].strip()
					)
				except AttributeError:
					try:
						player["Position"] = (
							tag.find(
								"td", class_="PositionWoTeam2"
							).get_text()
							.strip()
						)
					except:
						pass

				try:
					player["Join Date"] = (
						tag.find_all(
							"div", class_="Date"
						))
					if len(player["Join Date"]) > 1:
						player["Leave Date"] = (
							player["Join Date"][1]
							.get_text()
							.split()[0]
						)
						try:
							player["New Team"] = (
							tag.find(
								"td", class_="NewTeam"
							).get_text()
							.strip()
							)
						except:
							pass
					if player["Join Date"][0].get_text().split()[0] != []:
						player["Join Date"] = (
							player["Join Date"][0]
							.get_text()
							.split()[0]
						)
					else:
						del player["Join Date"]
					
				except:
					pass
				players_dict[title].append(player)

		return players_dict


	def get_team_achivements(self,soup):
		# empty list
		data = []
		
		# for getting the header from
		# the HTML file
		list_header = []
		header = soup.find_all("table")[0].find("tr")
		
		for items in header:
			try:
				list_header.append(items.get_text())
			except:
				continue
		
		list_header.append('icon')

		# for getting the data
		HTML_data = soup.find_all("table")[0].find_all("tr")[1:]
		
		for element in HTML_data:
			sub_data = []
			econ = ''
			for sub_element in element:
				try:
					econ = sub_element.find("span", class_="team-template-team-icon").a['title']	
				except:
					pass
				
				try:
					sub_data.append(sub_element.get_text())
				except:
					continue
			sub_data = [unicodedata.normalize("NFKD", ele).strip() for ele in sub_data]
			if len(sub_data) > len(list_header):
				del sub_data[3]
				val = ''
				while val in sub_data:
					sub_data.remove(val)
			
			if len(sub_data) > 6:
				sub_data[4:6] = [''.join(sub_data[4:6])]
			
			sub_data.append(econ)
			data.append(sub_data)
		
		# Storing the data into Pandas
		# DataFrame
		dataFrame = pd.DataFrame(data = data, columns = list_header)
		# print(data)
		# Converting Pandas DataFrame
		# into CSV file
		# dataFrame.to_csv('Geeks.csv')
		return dataFrame

	def get_played_match(self, soup):
		data = []
		# for getting the header from
		# the HTML file
		list_header = []
		header = soup.find_all("table")[0].find("tr")
		
		for items in header:
			try:
				list_header.append(items.get_text())
			except:
				continue
		# for getting the data
		HTML_data = soup.find_all("table")[0].find_all("tr")[1:]
			
		for element in HTML_data:
			sub_data = []
			vod = []
			for sub_element in element:
				try:
					sub_data.append(sub_element.a['title'])
				except:	
					sub_data.append(sub_element.get_text())

				try:
					if 'Watch' in sub_element.a['title']:
						vod.append(sub_element.a['href'])
				except:
					pass
			sub_data = [unicodedata.normalize("NFKD", ele).strip() for ele in sub_data]
			
			# vod exists length of potential data == 8
			if vod != []:
				expect_length = len(list_header)
			# vod does not exist: potential data == 7
			else:
				expect_length = len(list_header) - 1

			# data not full potentially time is missing
			if len(sub_data) == expect_length:
				time = ''
				sub_data.insert(1, time)
			
			# del duplicate tournament logo and name
			del sub_data[3]
			
			sub_data[6] = vod
			data.append(sub_data)
		dataFrame = pd.DataFrame(data = data, columns = list_header)
		
		# Converting Pandas DataFrame
		# into CSV file
		# dataFrame.to_csv('Geeks2.csv')
		return dataFrame