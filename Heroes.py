import json


class Heroes:

    @staticmethod
    def load_heroes():
        with open(r'database/heroes.json', 'r') as herodata:
            return json.loads(herodata.read())

    def save_heroes(self):
        with open(r'database/heroes.json', 'w') as herodata:
            herodata.write(json.dumps(self._heroes))

    @property
    def _heroes(self):
        return self.load_heroes()

    @property
    def sort_heroes_by_id(self):
        return {hero['id']: hero for hero in self._heroes}

    @property
    def sort_heroes_by_name(self):
        return {hero['localized_name']: hero for hero in self._heroes}

    @property
    def heroes(self):
        return self.sort_heroes_by_id
