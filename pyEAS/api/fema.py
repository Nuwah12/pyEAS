
from datetime import datetime
from typing import Dict
import requests
from requests.exceptions import HTTPError, RequestException
from .config import Settings

URL = Settings.FEMA.IPAWS_ARCHIVED

def _request(params: Dict, timeout: int = 15) -> Dict:
    """
    Send a request to FEMA's IPAWS archive.

    Parameters:
        params (dict) - Query parameters
        timeout (int) - seconds to wait before cancelling request
    """
    try:
        resp = requests.get(URL,
                            params = params,
                            timeout = timeout).json() ## TODO: test params 
        resp.raise_for_status()
        return resp.json()
    
    except requests.exceptions.Timeout:
        print(f"[TIMEOUT] Request timed out after {timeout}s")
    except requests.exceptions.HTTPError as e:
        print(f"[ERROR] HTTP Error {resp.status}: {e}")
    except ValueError:
        print("[ERROR] Response content is not valid JSON, aborting")

def get_historic_alert(date: datetime, **kwargs):

    ### TODO: Validate passed kwargs

    ### TODO: Parse kwargs into local dict

    ### TODO: Parse response into slimmer json

    _request(params = kwargs)