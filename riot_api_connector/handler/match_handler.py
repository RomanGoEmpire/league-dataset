import requests

MATCH_CALLS = {
    "match_ids_by_puuid": "/lol/match/v5/matches/by-puuid/{puuid}/ids",
    "match_by_match_id": "/lol/match/v5/matches/{matchId}",
    "match_timeline_by_match_id": "/lol/match/v5/matches/{matchId}/timeline"
}


class MatchHandler:

    def __init__(self, api_key):
        self.api_key = api_key
        self.regions = ["europe", "asia", "americas", "sea"]

    def match_list(self,
                   puuid,
                   region,
                   ):
        region = region.lower()
        if region not in self.regions:
            raise KeyError("Region not valid. Check .regions")
        url_match = f"https://{region}.api.riotgames.com{MATCH_CALLS["match_ids_by_puuid"]}?api_key={self.api_key}"
        url_match = url_match.format(puuid=puuid)
        response = requests.get(url_match)
        return response.json()
