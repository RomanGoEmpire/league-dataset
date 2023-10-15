from .basic_handler import Handler

MATCH_CALLS = {
    "match_ids_by_puuid": "/lol/match/v5/matches/by-puuid/{puuid}/ids",
    "match_by_match_id": "/lol/match/v5/matches/{matchId}",
    "match_timeline_by_match_id": "/lol/match/v5/matches/{matchId}/timeline"
}


class MatchHandler(Handler):

    def __init__(self, api_key):
        super().__init__(api_key)
        self.regions = ["europe", "asia", "americas", "sea"]

    def match_list(self, region, puuid, start_time=None, end_time=None, queue=None, type=None, start=None,
                   count=20) -> dict:
        if count > 100:
            raise ValueError("Count cannot be greater than 100")
        params = {
            "startTime": start_time,
            "endTime": end_time,
            "queue": queue,
            "type": type,
            "start": start,
            "count": count

        }
        params = {key: value for key, value in params.items() if value is not None}
        return self.make_request(region, MATCH_CALLS["match_ids_by_puuid"], params=params, puuid=puuid)

    def match(self, region, match_id) -> dict:
        return self.make_request(region, MATCH_CALLS["match_by_match_id"], matchId=match_id)

    def match_timeline(self, region, match_id) -> dict:
        return self.make_request(region, MATCH_CALLS["match_timeline_by_match_id"], matchId=match_id)
