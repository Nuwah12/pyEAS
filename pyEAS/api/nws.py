
from typing import Dict
import requests
from requests.exceptions import HTTPError, RequestException
from config import Settings

URL = Settings.NWS.ACTIVE_ALERTS
HEADERS = Settings.NWS.DEFAULT_HEADERS

def request(params: Dict, url: str, timeout: int = 15) -> Dict:
    return requests.get(URL,
                        params = params,
                        headers = HEADERS,
                        timeout = timeout).json() ## TODO: test params 