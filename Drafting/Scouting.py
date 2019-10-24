from Heroes import Heroes
from OpenDotA import OpenDotA


def load_api_key():
    with open('api.key', 'r') as key_file:
        return key_file.read().strip()


class Scouting:
    def __init__(self, open_dota):
        self.open_dota = open_dota
        self.heroes = Heroes()
        self.positions = {"1": None,
                          "2": None,
                          "3": None,
                          "4": None,
                          "5": None}

    def assign_localized_name(self, hero):
        hero['localized_name'] = self.heroes.heroes[int(hero['hero_id'])]['localized_name']
        return hero

    def get_account_id(self, steam_id):
        return self.open_dota.get_account_id(steam_id)

    def get_recent_heroes_pool(self, steam_id):
        # TODO: I don't think I can clean this up anymore than it already is
        matches = self.get_recent_matches(steam_id)
        return {self.heroes.heroes[match['hero_id']]['localized_name']: len(list(filter(lambda hero: hero['hero_id'] == match['hero_id'], matches))) for match in matches}

    def get_recent_matches(self, steam_id):
        return self.open_dota.get_recent_matches(steam_id)

    def get_heroes_pool(self, steam_id):
        return self.open_dota.get_heroes_pool(steam_id)

    def get_counts(self, steam_id):
        return self.open_dota.get_counts(steam_id)

    def get_rating(self, steam_id):
        return self.open_dota.get_rating(steam_id)

    def get_ranking(self, steam_id):
        return self.open_dota.get_ranking(steam_id)

    def get_best_hero(self, steam_id):
        return self.assign_localized_name(self.get_best_hero_by_score(steam_id))

    def get_best_hero_by_score(self, steam_id):
        return max(self.get_ranking(steam_id), key=lambda k: k['score'])

    def get_best_hero_by_ranking(self, steam_id):
        return max(self.get_ranking(steam_id), key=lambda k: k['percent_rank'])

    def get_most_likely_heroes(self, steam_id):
        return list(set([hero['hero_id'] for hero in self.get_recent_heroes_pool(steam_id)]))

    def get_most_played_hero(self, steam_id):
        return self.assign_localized_name(max(self.open_dota.get_heroes_pool(steam_id), key=lambda k: k['games']))

    def get_most_likely_lane(self, steam_id):
        # TODO: Finish this
        return self.get_counts(steam_id)

    def most_likely_positions(self, steam_id):
        # TODO: This is wrong. Fix. We want positions not likely heroes
        return self.get_most_likely_heroes(steam_id)


if __name__ == '__main__':
    API_KEY = load_api_key()
    hatchi = '74427895'
    neph = '285975878'
    firetoad = '120572176'
    sage = '31200766'
    pat = '85363222'
    rhys = '79676403'
    jesse = '82758096'

    players_list = [hatchi, sage, neph, firetoad, pat, rhys, jesse]
    open_dota = OpenDotA(API_KEY)
    scouting = Scouting(open_dota)

    # TODO: At some point I want to make this threaded for multiple API calls running at once.
    for player in players_list:
        search_person = player
        account_id = scouting.get_account_id(search_person)
        counts = open_dota.get_counts(search_person)
        recent_heroes = scouting.get_recent_heroes_pool(search_person)
        ranking = scouting.get_ranking(search_person)
        best_hero = scouting.get_best_hero(search_person)
        rating = scouting.get_rating(search_person)
        most_played = scouting.get_most_played_hero(search_person)

        print(f'Scouting Report for {account_id["profile"]["personaname"]} - Steam ID: {search_person}')
        print(f'Best Hero: {best_hero["localized_name"]} - {best_hero["score"]}')
        print(f'Most Recent Heroes: {recent_heroes}')
        print(f'Most Played Hero: {most_played["localized_name"]} - Games: {most_played["games"]}')
        print(f"")
