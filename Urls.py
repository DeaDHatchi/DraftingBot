class Urls:
    def __init__(self, API_KEY):
        self.base_url = 'https://api.opendota.com/api'
        self.api_key = API_KEY

    @property
    def api(self):
        return f'?api_key={self.api_key}'

    @property
    def heroStats(self):
        return f'{self.base_url}/heroStats{self.api}'
