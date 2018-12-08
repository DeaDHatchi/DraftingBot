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


class Player:
    def __init__(self, steamid, opendota):
        self.steamid = steamid
        self.opendota = opendota

    @property
    def recentMatches(self):
        return self.opendota.getRecentMatches(self.steamid)

    @property
    def matches(self):
        return self.opendota.getMatches(self.steamid)

    @property
    def rankings(self):
        return self.opendota.getRanking(self.steamid)


class OpenDotA:
    def __init__(self, API_KEY):
        self.api_key = API_KEY
        self.urls = Urls(self.api_key)
        self.players = Players(self.api_key)

    def get(self, url):
        return json.loads(self.response(url).text)

    def response(self, url):
        return requests.get(url)

    def getMatches(self, steamid):
        return self.get(self.players.matches(steamid))

    def getRecentMatches(self, steamid):
        return self.get(self.players.recentMatches(steamid))

    def getHeroesPool(self, steamid):
        return self.get(self.players.heroes(steamid))

    def getRanking(self, steamid):
        return self.get(self.players.rankings(steamid))

    def getRankings(self, steamids):
        returndict = {}
        for steamid in steamids:
            returndict[steamid] = self.getRanking(steamid)
        return returndict


class Scouting:
    def __init__(self, opendota):
        self.opendota = opendota
        self.positions = {"1": None,
                          "2": None,
                          "3": None,
                          "4": None,
                          "5": None}

    def getRecentHeroesPool(self, steamid):
        pool = {}
        matches = self.opendota.getRecentMatches(steamid)
        for match in matches:
            if match['hero_id'] in pool:
                pool[match['hero_id']] += 1
            else:
                pool[match['hero_id']] = 1
        return pool

    def getHeroesPool(self, steamid):
        return self.opendota.getHeroesPool(steamid)

    def calcMostLikelyPositions(self, steamids):
        mostlikelypositions = {}
        for steamid in steamids:
            mostlikelypositions[steamid] = self.getRecentHeroesPool(steamid)
        return mostlikelypositions

    def mostLikelyPositions(self, steamids):
        return self.calcMostLikelyPositions(steamids)


players_list = [Hatchi, sage, neph, firetoad, pat]

opendota = OpenDotA(API_KEY)
scouting = Scouting(opendota)

test1 = scouting.calcMostLikelyPositions(players_list)

print('debugline')