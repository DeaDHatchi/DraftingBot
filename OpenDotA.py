import requests
import json
from urls import Urls, Players
from Main import Heroes

API_KEY = '8467cd42-abd7-4189-a4c0-1b65eca157d'
heroes = Heroes()

Hatchi = '74427895'
neph = '285975878'
firetoad = '120572176'
sage = '31200766'
pat = '85363222'


class OpenDotA:
    def __init__(self, API_KEY):
        self.api_key = API_KEY
        self.urls = Urls(self.api_key)
        self.players = Players(self.api_key)

    def get(self, url):
        return json.loads(self.response(url).text)

    def response(self, url):
        return requests.get(url)

opendota = OpenDotA(API_KEY)

hatchi_profile = opendota.get(opendota.players.account_id(Hatchi))
neph_profile = opendota.get(opendota.players.account_id(neph))
firetoad_profile = opendota.get(opendota.players.account_id(firetoad))
sage_profile = opendota.get(opendota.players.account_id(sage))
pat_profile = opendota.get(opendota.players.account_id(pat))

hatchi_recent_matches = opendota.get(opendota.players.recentMatches(Hatchi))

hatchi_matches = opendota.get(opendota.players.matches(Hatchi))

hatchi_peers = opendota.get(opendota.players.peers(Hatchi))

stats = opendota.get(opendota.urls.heroStats)

for hero in stats:
    hero['pro_winrate'] = hero['pro_win'] / hero['pro_pick']

highest_winrate = sorted(stats, key=lambda x: x['pro_winrate'], reverse=True)

for hero in highest_winrate:
    print('Hero: {} - Winrate - {}'.format(hero['localized_name'], hero['pro_win'] / hero['pro_pick']))

print('debugline')