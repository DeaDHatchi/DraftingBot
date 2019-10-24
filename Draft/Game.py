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