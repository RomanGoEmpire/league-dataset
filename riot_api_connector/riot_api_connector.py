from handler import MatchHandler

HTTP_STATUS_CODES = {
    400: 'Bad request',
    401: 'Unauthorized',
    403: 'Forbidden',
    404: 'Data not found',
    405: 'Method not allowed',
    415: 'Unsupported media type',
    429: 'Rate limit exceeded',
    500: 'Internal server error',
    502: 'Bad gateway',
    503: 'Service unavailable',
    504: 'Gateway timeout'
}


class RiotApiConnector:

    def __init__(self, api_key: str):
        self.api_key = self.verify_api_key(api_key)
        self.match = MatchHandler(self.api_key)

    @staticmethod
    def verify_api_key(api_key):
        expected_length = 42
        hyphen_positions = [5, 14, 19, 24, 29]
        if not (len(api_key) == expected_length and all(api_key[i] == '-' for i in hyphen_positions)):
            raise ValueError(f"{api_key} has an invalid form")
        return api_key
