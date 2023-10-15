from .basic_handler import Handler


class SummonerHandler(Handler):

    def __init__(self, api_key):
        super().__init__(api_key)
        self.regions = ["br1", "eun1", "euw1", "jp1", "kr", "la1", "la2", "na1", "oc1", "tr1", "ru", "ph2", "sg2",
                        "th2", "tw2", "vn2"]
        self._summoner_calls = {
            "summoner_by_name": "/lol/summoner/v4/summoners/by-name/{summonerName}",
            "summoner_by_puuid": "/lol/summoner/v4/summoners/by-puuid/{encryptedPUUID}",
            "summoner_by_account_id": "/lol/summoner/v4/summoners/by-account/{encryptedAccountId}",
        }

    def by_name(self, region, name):
        return self.make_request(region, self._summoner_calls["summoner_by_name"], summonerName=name)

    def by_puuid(self, region, puuid):
        return self.make_request(region, self._summoner_calls["summoner_by_puuid"], encryptedPUUID=puuid)

    def by_account_id(self, region, account_id):
        return self.make_request(region, self._summoner_calls["summoner_by_account_id"], encryptedAccountId=account_id)
