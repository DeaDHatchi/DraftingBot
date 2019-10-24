class Urls:
    def __init__(self, API_KEY):
        self.base_url = 'https://api.opendota.com/api'
        self.api_key = API_KEY

    def append_api_key(self, url):
        return f'{url}?{self.api_key}'

    @property
    def heroStats(self):
        return f'{self.base_url}/heroStats'


class OpenDotAAccount(Urls):
    def __init__(self, API_KEY):
        super().__init__(API_KEY)

    @property
    def players(self):
        return f'{self.base_url}/players'

    def account_id(self, account_id):
        return f'{self.players}/{account_id}'

    def wl(self, account_id):
        return f'{self.account_id(account_id)}/wl'

    def recent_matches(self, account_id):
        return f'{self.account_id(account_id)}/recentMatches'

    def matches(self, account_id):
        return f'{self.account_id(account_id)}/matches'

    def heroes(self, account_id):
        return f'{self.account_id(account_id)}/heroes'

    def peers(self, account_id):
        return f'{self.account_id(account_id)}/peers'

    def counts(self, account_id):
        return f'{self.account_id(account_id)}/counts'

    def histograms(self, account_id):
        return f'{self.account_id(account_id)}/histograms'

    def wardmap(self, account_id):
        return f'{self.account_id(account_id)}/wardmap'

    def wordcloud(self, account_id):
        return f'{self.account_id(account_id)}/wordcloud'

    def ratings(self, account_id):
        return f'{self.account_id(account_id)}/ratings'

    def rankings(self, account_id):
        return f'{self.account_id(account_id)}/rankings'
