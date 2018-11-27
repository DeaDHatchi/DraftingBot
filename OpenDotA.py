import requests
import json
from Main import Heroes

API_KEY = '8467cd42-abd7-4189-a4c0-1b65eca157d'
Hatchi = '74427895'
base_url = 'https://api.opendota.com/api'
heroes = Heroes()

response = requests.get(url='{}/players/{}?{}'.format(base_url, Hatchi, API_KEY))

Hatchi_Profile = json.loads(response.text)

response = requests.get(url='{}/players/{}/recentMatches?{}'.format(base_url, Hatchi, API_KEY))
recent_matches = json.loads(response.text)

response = requests.get(url='{}/heroes/8/matchups?{}'.format(base_url, API_KEY))
jugg_matchups = json.loads(response.text)

for hero in jugg_matchups:
    print('Hero: {} - Winrate: {}'.format(heroes.heroes[hero['hero_id']]['localized_name'], hero['wins'] / hero['games_played']))


print('debugline')