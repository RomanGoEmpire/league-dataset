import warnings
HOSTS = {
    "BR1": "br1.api.riotgames.com",
    "EUN1": "eun1.api.riotgames.com",
    "EUW1": "euw1.api.riotgames.com",
    "JP1": "jp1.api.riotgames.com",
    "KR": "kr.api.riotgames.com",
    "LA1": "la1.api.riotgames.com",
    "LA2": "la2.api.riotgames.com",
    "NA1": "na1.api.riotgames.com",
    "OC1": "oc1.api.riotgames.com",
    "TR1": "tr1.api.riotgames.com",
    "RU": "ru.api.riotgames.com",
    "PH2": "ph2.api.riotgames.com",
    "SG2": "sg2.api.riotgames.com",
    "TH2": "th2.api.riotgames.com",
    "TW2": "tw2.api.riotgames.com",
    "VN2": "vn2.api.riotgames.com",
}


class RiotApiConnector:

    def __init__(self, api_key: str, region=None):
        self.api_key = self.verify_api_key(api_key)
        self.host = self.verify_region(region)

    @staticmethod
    def regions():
        return list(HOSTS.keys())

    @staticmethod
    def verify_api_key(api_key):
        expected_length = 42
        hyphen_positions = [5, 14, 19, 24, 29]
        if not (len(api_key) == expected_length and all(api_key[i] == '-' for i in hyphen_positions)):
            raise ValueError(f"{api_key} has an invalid form")
        return api_key

    @staticmethod
    def verify_region(region):
        if region is None:
            warnings.warn("No region selected",Warning)
            return None

        region_key = region.upper()

        if region_key not in HOSTS.keys():
            raise KeyError(f"{region} not supported. The 'regions()' returns all possible options")
        return HOSTS[region_key]
