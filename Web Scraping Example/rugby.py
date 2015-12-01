import requests, csv, unicodecsv
from bs4 import BeautifulSoup


'''For all rugby fans! This script pulls each player's information that is available on the RWC 2015 website. You can use this template to make changes so that you can pull from other websites as well'''


main_url = "http://www.rugbyworldcup.com"
teams_url = "http://www.rugbyworldcup.com/teams"


#retrieve each team's url
print "Retrieving countries\' url"
r = requests.get(teams_url)
#spits all html content out
soup = BeautifulSoup(r.content)

links = soup.find_all("a", {"class":"teamBlock"})

teams_array =[]

for link in links:
	country = link.get("href")
	squad = "/squad"
	country_url = main_url + country + squad
	teams_array.append(country_url)

print "Retrieval complete"


players_array = []

#retrieve each player's url 
print "Retrieving player url"
for link in teams_array:
	r = requests.get(link)
	new_soup = BeautifulSoup(r.content)

	players = new_soup.find_all("a", {"class":"player"})
		

	for link in players:
		player = link.get("href")
		player_url = main_url + player
		players_array.append(player_url)

print "Retrieval complete"



rugby = unicodecsv.writer(open("rugbyworldcup.csv","wt"))

#retrieve each player's full information
#some player's information are messed up, so you will see some try except commands added
print "Retrieving player information"
for link in players_array:
	r = requests.get(link)
	new_soup = BeautifulSoup(r.content)

	name_tag = new_soup.find("h2", {"class":"name"})
	caps_tag = new_soup.find("h4", {"class":"caps"})
	stats_tag = new_soup.find_all("h4", {"class":"info"})
	


	team_info = new_soup.find("h4", {"class":"team"})
	try:
		team_tag = team_info.contents[5] #pull country tag from #team
	except:
		pass


	#retrieve each tag in stats_tag list
	position_tag = stats_tag[0]
	debut_tag = stats_tag[1]
	age_tag = stats_tag[2]
	height_tag = stats_tag[3]
	weight_tag = stats_tag[4]
	matches_tag = stats_tag[5]
	points_tag = stats_tag[6]
	tries_tag = stats_tag[7]
	yellows_tag = stats_tag[8]
	try:
		reds_tag = stats_tag[9]
	except: 
		pass

	#pulls strings out of each tag
	name = name_tag.string
	try:
		team = team_tag.string
	except:
		team = "N/A"
	try:
		caps = caps_tag.string
	except:
		caps = "N/A"
	position = position_tag.string
	debut = debut_tag.string
	age = age_tag.string
	height = height_tag.string
	weight = weight_tag.string
	matches = matches_tag.string
	points = points_tag.string
	tries = tries_tag.string
	yellows = yellows_tag.string
	try:
		reds = reds_tag.string
	except:
		reds = "N/A"


	
	rugby.writerow([name, team, caps, position, debut, age, height, weight, matches, points, tries, yellows, reds])
	
	print "finished going through player", name, "from", team 
	
print "RWC 2015 player information now ready"




		
