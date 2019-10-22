import json

import requests

from Heroes import Heroes
from urls import Urls, OpenDotAAccount


def load_api_key():
    with open('api.key', 'r') as keyfile:
        return keyfile.read().strip()


API_KEY = load_api_key()
heroes = Heroes()

Hatchi = '74427895'
neph = '285975878'
firetoad = '120572176'
sage = '31200766'
pat = '85363222'
rhys = '79676403'
jesse = '82758096'


class Player:
    def __init__(self, steam_id, open_dota):
        """
        Object representing a Players Demographic information from OpenDotA
        :param steam_id: String
        :param open_dota: String
        """
        self.steam_id = steam_id
        self.open_dota = open_dota

    @property
    def account_id(self):
        return self.open_dota.get_account_id(self.steam_id)

    @property
    def persona_name(self):
        return self.account_id['profile']['personaname']

    @property
    def recent_matches(self):
        """
        Returns a list of recent matches from the Player
        :return: list
        """
        return self.open_dota.get_recent_matches(self.steam_id)

    @property
    def matches(self):
        """
        Returns all matches of a Player
        :return: List
        """
        return self.open_dota.get_matches(self.steam_id)

    @property
    def rankings(self):
        """
        Returns Ranking for a given player
        :return:
        """
        return self.open_dota.get_ranking(self.steam_id)

    @property
    def counts(self):
        return self.open_dota.get_counts(self.steam_id)


class OpenDotA:
    def __init__(self, API_KEY):
        self.api_key = API_KEY
        self.urls = Urls(self.api_key)
        self.players = OpenDotAAccount(self.api_key)

    def get(self, url):
        """
        Basic Get request
        :param url: String
        :return: Json Object
        """
        return json.loads(self.response(url).text)

    def response(self, url):
        """
        Return a Requests Object from the URL Response
        :param url: String
        :return: Requests Object
        """
        return requests.get(url)

    def get_account_id(self, steam_id):
        return self.get(self.players.account_id(steam_id))

    def get_matches(self, steam_id):
        return self.get(self.players.matches(steam_id))

    def get_counts(self, steam_id):
        return self.get(self.players.counts(steam_id))

    def get_recent_matches(self, steam_id):
        return self.get(self.players.recent_matches(steam_id))

    def get_heroes_pool(self, steam_id):
        return self.get(self.players.heroes(steam_id))

    def get_rating(self, steam_id):
        return self.get(self.players.ratings(steam_id))

    def get_ranking(self, steam_id):
        return self.get(self.players.rankings(steam_id))

    def get_rankings(self, steam_ids):
        return {steam_id: self.get_ranking(steam_id) for steam_id in steam_ids}


class Scouting:
    def __init__(self, open_dota):
        self.open_dota = open_dota
        self.heroes = Heroes()
        self.positions = {"1": None,
                          "2": None,
                          "3": None,
                          "4": None,
                          "5": None}

    def get_account_id(self, steam_id):
        return self.open_dota.get_account_id(steam_id)

    def get_recent_heroes_pool(self, steam_id):
        # TODO: I don't think I can clean this up anymore than it already is
        matches = self.get_recent_matches(steam_id)
        return {self.heroes.heroes[match['hero_id']]['localized_name']:
                    len([heroes for hero in matches if hero['hero_id'] == match['hero_id']]) for match in matches}

    def get_recent_matches(self, steam_id):
        return self.open_dota.get_recent_matches(steam_id)

    def get_heroes_pool(self, steam_id):
        return self.open_dota.get_heroes_pool(steam_id)

    def get_rating(self, steam_id):
        return self.open_dota.get_rating(steam_id)

    def get_ranking(self, steam_id):
        return self.open_dota.get_ranking(steam_id)

    def get_best_hero(self, steam_id):
        # TODO: How can we clean this up?
        best = self.get_best_hero_by_score(steam_id)
        best['localized_name'] = self.heroes.sort_heroes_by_id[best['hero_id']]['localized_name']
        return best

    def get_best_hero_by_score(self, steam_id):
        return max(self.get_ranking(steam_id), key=lambda k: k['score'])

    def get_best_hero_by_ranking(self, steam_id):
        return max(self.get_ranking(steam_id), key=lambda k: k['percent_rank'])

    def get_most_likely_heroes(self, steam_ids):
        # TODO: This is wrong. Fix. We want Top Played Heroes. Not Recent Heroes
        return {steam_id: self.get_recent_heroes_pool(steam_id) for steam_id in steam_ids}

    def most_likely_positions(self, steam_ids):
        # TODO: This is wrong. Fix. We want postions not likely heroes
        return self.get_most_likely_heroes(steam_ids)


if __name__ == '__main__':
    players_list = [Hatchi, sage, neph, firetoad, pat, rhys, jesse]
    opendota = OpenDotA(API_KEY)
    scouting = Scouting(opendota)

    for player in players_list:
        search_person = player
        account_id = scouting.get_account_id(search_person)
        counts = opendota.get_counts(search_person)
        recent_heroes = scouting.get_recent_heroes_pool(search_person)
        ranking = scouting.get_ranking(search_person)
        best_hero = scouting.get_best_hero(search_person)
        rating = scouting.get_rating(search_person)

        print(f'Scouting Report for {account_id["profile"]["personaname"]} - {search_person}')
        print(f'Best Hero: {best_hero["localized_name"]} - {best_hero["score"]}')
        print(f'Most Recent Heroes: {recent_heroes}\n')

