import json

from Heroes import Heroes


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

    def __init__(self, ident):
        self.ident = ident
        self.role = self._roles[self.ident]


class Bot:
    _default_order = [5, 4, 3, 1, 2]
    _off_lane_priority_order = [5, 1, 2, 4, 3]
    _safe_lane_priority_order = [4, 3, 2, 5, 1]
    _early_cores_order = [1, 2, 3, 4, 5]
    _mid_lane_priority_order = [3, 4, 5, 1, 2]

    def __init__(self):
        self.positions = [1, 2, 3, 4, 5]


class Drafting:
    _order = [10, 20, 10, 20, 10, 20, 1, 2, 2, 1, 10, 20, 10, 20, 2, 1, 2, 1, 20, 10, 1, 2]

    def __init__(self, starting_side='Radiant'):
        self.game = Game()
        self.heroes = Heroes()
        self.starting = starting_side

    @property
    def draft(self):
        return {'radiant': {'picks': self.game.radiant.picks,
                            'bans': self.game.radiant.bans},
                'dire': {'picks': self.game.dire.picks,
                         'bans': self.game.dire.bans}}

    def save_draft(self):
        with open(r'database\draft.json', 'w') as draft_data:
            draft_data.write(json.dumps(self.draft))

    @staticmethod
    def selection(side, pick_or_ban):
        return int(input(f'Select a hero for {side} to {pick_or_ban} by id: '))

    def radiant_pick(self):
        print('Radiant Pick')
        selection = self.selection('Radiant', 'Pick')
        self.game.radiant.add_pick(self.heroes.heroes[selection])
        print('Radiant Drafted {}\n'.format(self.heroes.heroes[selection]['localized_name']))

    def radiant_ban(self):
        print('Radiant Ban')
        selection = self.selection('Radiant', 'Ban')
        self.game.radiant.add_ban(self.heroes.heroes[selection])
        print('Radiant Banned {}\n'.format(self.heroes.heroes[selection]['localized_name']))

    def dire_pick(self):
        print('Dire Pick')
        selection = self.selection('Dire', 'Pick')
        self.game.dire.add_pick(self.heroes.heroes[selection])
        print('Dire Drafted {}\n'.format(self.heroes.heroes[selection]['localized_name']))

    def dire_ban(self):
        print('Dire Ban')
        selection = self.selection('Dire', 'Ban')
        self.game.dire.add_ban(self.heroes.heroes[selection])
        print('Dire Banned {}\n'.format(self.heroes.heroes[selection]['localized_name']))

    def lets_draft(self):
        # TODO: I could probably clean this up even more. Don't quite know how yet?
        if self.starting == 'Radiant':
            for choice in self._order:
                if choice == 1:  # Radiant Pick
                    self.radiant_pick()
                if choice == 2:  # Dire Pick
                    self.dire_pick()
                if choice == 10:  # Radiant Ban
                    self.radiant_ban()
                if choice == 20:  # Dire Ban
                    self.dire_ban()
        else:
            for choice in self._order:
                if choice == 1:  # Dire Pick
                    self.dire_pick()
                if choice == 2:  # Radiant Pick
                    self.radiant_pick()
                if choice == 10:  # Dire Ban
                    self.dire_ban()
                if choice == 20:  # Radiant Ban
                    self.radiant_ban()
        self.announce_draft()
        self.save_draft()

    def announce_draft(self):
        print('Picks')
        print('Radiant Draft: {}'.format(', '.join(self.game.radiant.picks_printout())))
        print('Dire Draft: {}\n'.format(', '.join(self.game.dire.picks_printout())))
        print('Bans')
        print('Radiant Bans: {}'.format(', '.join(self.game.radiant.bans_printout())))
        print('Dire Bans: {}\n'.format(', '.join(self.game.dire.bans_printout())))


class Game:
    def __init__(self):
        self.radiant = Side()
        self.dire = Side()

    @property
    def bans(self):
        return self.radiant.bans + self.dire.bans

    @property
    def picks(self):
        return self.radiant.picks + self.dire.picks


class Side:
    def __init__(self):
        self.bans = []
        self.picks = []

    def add_ban(self, hero):
        self.bans.append(hero)

    def add_pick(self, hero):
        self.picks.append(hero)

    def bans_printout(self):
        return [ban['localized_name'] for ban in self.bans]

    def picks_printout(self):
        return [pick['localized_name'] for pick in self.picks]


if __name__ == '__main__':
    main = Main()
    main.run()
    print('debugline')
