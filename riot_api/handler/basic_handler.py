import requests


class Handler:
    BASE_URL = "https://{region}.api.riotgames.com"

    def __init__(self, api_key):
        self._api_key = api_key
        self.regions = None

    def is_valid_region(self, region) -> bool:
        if region.lower() not in self.regions:
            raise KeyError("Region not valid. Check .regions")
        return True

    def make_request(self, region, call, params=None, **kwargs) -> dict:
        if params is None:
            params = {}
        params["api_key"] = self._api_key

        url = self.build_url(region, call, **kwargs)
        response = requests.get(url, params=params)
        return response.json()

    def build_url(self, region, call, **kwargs) -> str:
        if not self.is_valid_region(region):
            raise ValueError(f"Invalid region. Options are: {self.regions}")

        formatted_url = self.BASE_URL + call
        return formatted_url.format(region=region, **kwargs)
