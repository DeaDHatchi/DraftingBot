import json


class Main:
    def __init__(self):
        self.state = True

    def exit(self):
        self.state = False

    def run(self):
        while self.state:
            self.lets_draft()

    def lets_draft(self):
        draft = Drafting()
        draft.lets_draft()
        choice = input('Do you want to draft again? (Y/N): ')
        if choice.upper() == 'Y':
            self.lets_draft()
        else:
            self.exit()


class Position:

    _roles = {1: 'Carry',
              2: 'Mid',
              3: 'Offlane',
              4: 'Flex',
              5: 'Support'}

    def __init__(self, id):
        self.id = id
        self.role = self._roles[self.id]


class Bot:

    _default_order = [5, 4, 3, 1, 2]
    _offlane_priority_order = [5, 1, 4, 3, 2]
    _safelane_priority_order = [4, 3, 5, 2, 1]

    def __init__(self):
        self.positions = [1, 2, 3, 4, 5]


class Drafting:

    _order = [10, 20, 10, 20, 10, 20, 1, 2, 2, 1, 10, 20, 10, 20, 2, 1, 2, 1, 20, 10, 1, 2]

    def __init__(self, starting='Radiant'):
        self.game = Game()
        self.heroes = Heroes()
        self.starting = starting

    @property
    def draft(self):
        return {'radiant': {'picks': self.game.radiant.picks,
                            'bans': self.game.radiant.bans},
                'dire': {'picks': self.game.dire.picks,
                         'bans': self.game.dire.bans}}

    def save_draft(self):
        with open(r'database\draft.json', 'w') as draftdata:
            draftdata.write(json.dumps(self.draft))

    def lets_draft(self):
        if self.starting == 'Radiant':
            for choice in self._order:
                if choice == 1:
                    # Radiant Pick
                    print('Radiant Pick')
                    selection = int(input('Select a hero for Radiant to Pick by id: '))
                    self.game.radiant.add_pick(self.heroes.heroes[selection])
                    self.game.update_picks()
                    print('Radiant Drafted {}\n'.format(self.heroes.heroes[selection]['localized_name']))
                if choice == 2:
                    # Dire Pick
                    print('Dire Pick')
                    selection = int(input('Select a hero for Dire to Pick by id: '))
                    self.game.dire.add_pick(self.heroes.heroes[selection])
                    self.game.update_picks()
                    print('Dire Drafted {}\n'.format(self.heroes.heroes[selection]['localized_name']))
                if choice == 10:
                    # Radiant Ban
                    print('Radiant Ban')
                    selection = int(input('Select a hero for Radiant to Ban by id: '))
                    self.game.radiant.add_ban(self.heroes.heroes[selection])
                    self.game.update_bans()
                    print('Radiant Banned {}\n'.format(self.heroes.heroes[selection]['localized_name']))
                if choice == 20:
                    # Dire Ban
                    print('Dire Ban')
                    selection = int(input('Select a hero for Dire to Ban by id: '))
                    self.game.dire.add_ban(self.heroes.heroes[selection])
                    self.game.update_bans()
                    print('Dire Banned {}\n'.format(self.heroes.heroes[selection]['localized_name']))
        else:
            for choice in self._order:
                if choice == 1:
                    # Dire Pick
                    print('Dire Pick')
                    selection = int(input('Select a hero for Dire to Pick by id: '))
                    self.game.dire.add_pick(self.heroes.heroes[selection])
                    self.game.update_picks()
                    print('Dire Drafted {}\n'.format(self.heroes.heroes[selection]['localized_name']))
                if choice == 2:
                    # Radiant Pick
                    print('Radiant Pick')
                    selection = int(input('Select a hero for Radiant to Pick by id: '))
                    self.game.radiant.add_pick(self.heroes.heroes[selection])
                    self.game.update_picks()
                    print('Radiant Drafted {}\n'.format(self.heroes.heroes[selection]['localized_name']))
                if choice == 10:
                    # Dire Ban
                    print('Dire Ban')
                    selection = int(input('Select a hero for Dire to Ban by id: '))
                    self.game.dire.add_ban(self.heroes.heroes[selection])
                    self.game.update_bans()
                    print('Dire Banned {}\n'.format(self.heroes.heroes[selection]['localized_name']))
                if choice == 20:
                    # Radiant Ban
                    print('Radiant Ban')
                    selection = int(input('Select a hero for Radiant to Ban by id: '))
                    self.game.radiant.add_ban(self.heroes.heroes[selection])
                    self.game.update_bans()
                    print('Radiant Banned {}\n'.format(self.heroes.heroes[selection]['localized_name']))
        self.announce_draft()
        self.save_draft()

    def announce_draft(self):
        print('Radiant Draft: {}'.format(self.game.radiant.picks))
        print('Dire Draft: {}\n'.format(self.game.dire.picks))


class Game:

    _bans = []
    _picks = []

    def __init__(self):
        self.radiant = Side()
        self.dire = Side()

    def update_bans(self):
        self._bans = self.radiant.bans + self.dire.bans

    def update_picks(self):
        self._picks = self.radiant.picks + self.dire.picks


class Side:

    def __init__(self):
        self._bans = []
        self._picks = []

    def add_ban(self, hero):
        self._bans.append(hero)

    def add_pick(self, hero):
        self._picks.append(hero)

    @property
    def bans(self):
        return self._bans

    @property
    def picks(self):
        return self._picks


class Heroes:

    _heroes = {}
    _sorted_heroes = {}

    def __init__(self):
        self.load_heroes()
        self.sort_heroes_by_id()

    def load_heroes(self):
        with open(r'database/heroes.json', 'r') as herodata:
            self._heroes = json.loads(herodata.read())

    def save_heroes(self):
        with open(r'database/heroes.json', 'w') as herodata:
            herodata.write(json.dumps(self._heroes))

    def sort_heroes_by_id(self):
        sorted_heroes = {}
        for hero in self._heroes:
            sorted_heroes[hero['id']] = hero
        self._sorted_heroes = sorted_heroes

    @property
    def heroes(self):
        return self._sorted_heroes


if __name__ == '__main__':
    main = Main()
    main.run()
    print('debugline')

