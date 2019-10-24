import json

import requests

from Draft.Urls import OpenDotAAccount


class Player:
    # TODO: Am I even using this class? Why does it exists?
    # TODO: I might want to use this later for saving players.
    def __init__(self, steam_id, open_dota):
        """
        Object representing a Players information from OpenDotA
        :param steam_id: String
        :param open_dota: OpenDotA Object
        """
        self.steam_id = steam_id
        self.open_dota = open_dota

    @property
    def account_id(self):
        """
        Returns the Account information of a given Steam ID
        :return: Dictionary
        """
        return self.open_dota.get_account_id(self.steam_id)

    @property
    def persona_name(self):
        """
        Returns the Persona Name of the given Steam ID
        :return: String
        """
        return self.account_id['profile']['personaname']

    @property
    def recent_matches(self):
        """
        Returns a list of the most recent 20 matches from the given Steam ID
        :return: list
        """
        return self.open_dota.get_recent_matches(self.steam_id)

    @property
    def matches(self):
        """
        Returns all matches of a given Steam ID
        :return: List
        """
        return self.open_dota.get_matches(self.steam_id)

    @property
    def rankings(self):
        """
        Returns Ranking information for a given Steam ID
        :return: Dictionary
        """
        return self.open_dota.get_ranking(self.steam_id)

    @property
    def counts(self):
        """
        Returns counts information for a given Steam ID
        :return: Dictionary
        """
        return self.open_dota.get_counts(self.steam_id)


class OpenDotA:
    def __init__(self, api_key):
        self.account = OpenDotAAccount(api_key)

    def get(self, url):
        """
        Basic Get request
        :param url: String
        :return: Json Object
        """
        return json.loads(self.response(url).text)

    @staticmethod
    def response(url):
        """
        Return a Requests Object from the URL Response
        :param url: String
        :return: Requests Object
        """
        return requests.get(url)

    def get_account_id(self, steam_id):
        """
        Returns the Account ID of a given Steam ID
        :param steam_id: String
        :return: Dictionary
        """
        return self.get(self.account.account_id(steam_id))

    def get_matches(self, steam_id):
        """
        Returns all of the matches for a given Steam ID
        :param steam_id: String
        :return: List
        """
        return self.get(self.account.matches(steam_id))

    def get_counts(self, steam_id):
        """
        Returns the counts of a given Steam ID
        :param steam_id: String
        :return: Dictionary
        """
        return self.get(self.account.counts(steam_id))

    def get_recent_matches(self, steam_id):
        """
        Returns a list of the most recent 20 matches of a given Steam ID
        :param steam_id: String
        :return: List
        """
        return self.get(self.account.recent_matches(steam_id))

    def get_heroes_pool(self, steam_id):
        """
        Returns a list of all of the statistics for heroes played of a given Steam ID
        :param steam_id: String
        :return: List
        """
        return self.get(self.account.heroes(steam_id))

    def get_peers(self, steam_id):
        """
        Returns a list of peers for the given Steam ID
        :param steam_id: String
        :return: List
        """
        return self.get(self.account.peers(steam_id))

    def get_rating(self, steam_id):
        """
        Returns the competitive ratings of a given Steam ID
        :param steam_id: String
        :return: List
        """
        return self.get(self.account.ratings(steam_id))

    def get_ranking(self, steam_id):
        """
        Returns the rankings for heroes of a given Steam ID
        :param steam_id: String
        :return: List
        """
        return self.get(self.account.rankings(steam_id))

    def get_rankings(self, steam_ids):
        """
        Returns a dictionary of rankings for heroes of given Steam IDs
        :param steam_ids: List
        :return: Dictionary
        """
        return {steam_id: self.get_ranking(steam_id) for steam_id in steam_ids}
