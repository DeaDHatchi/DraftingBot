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

    def getRanking(self, steamid):
        return self.get(self.players.rankings(steamid))

    def getRankings(self, steamids):
        returndict = {}
        for steamid in steamids:
            returndict[steamid] = self.getRanking(steamid)
        return returndict



opendota = OpenDotA(API_KEY)

x = opendota.getRankings([Hatchi, sage, neph, firetoad, pat])

print('debugline')