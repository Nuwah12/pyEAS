
from typing import Dict, Optional
import requests
from requests.exceptions import HTTPError, RequestException
from .config import Settings

URL = Settings.NWS.ACTIVE_ALERTS
HEADERS = Settings.NWS.DEFAULT_HEADERS
VALID_STATUS = [""]

def _request(params: Dict, URL: str = URL, timeout: int = 15) -> Dict:
    """
    Send a request to the NWS's active alerts API.

    Parameters:
        params (dict) - Query parameters
        timeout (int) - seconds to wait before cancelling request
    """
    try:
        resp = requests.get(URL,
                            params = params,
                            headers = HEADERS,
                            timeout = timeout) ## TODO: test params 
        resp.raise_for_status()
        return resp.json()
    
    except requests.exceptions.Timeout:
        print(f"[TIMEOUT] Request timed out after {timeout}s")
    except requests.exceptions.HTTPError as e:
        print(f"[ERROR] HTTP Error {resp.status}: {e}")
    except ValueError:
        print("[ERROR] Response content is not valid JSON, aborting")

def get_active_alerts(
    area: str = "PA", # Default to PA
    status: str = "actual",
    point: Optional[tuple[str, str]] = None,
    **kwargs # all others
) -> Dict:
    """
    Fetch active alerts from NWS API.
    
    Parameters:
        area (str): UGC area code (optional)
        point (tuple[str, str]): (lat, lon) coordinates
        status (str): One of "Actual", "Exercise", "System", "Test", "Draft"
        **kwargs: Any extra query params (passed through)
    """

    ### TODO: Handle two different types of arguments that will be trated the same by the user:
    ###         1. Arguments passed via URL
    ###         2. Arguments that require filterting of response
    ### Obviously these have to be trated differently, but it'd be good for the user to be able to treat them  the same 
    valid_keys = Settings.NWS.VALID_SEARCH_KEYS
    params_use = {}
    for i in kwargs:
        if i not in valid_keys:         # Checking param name
            print(f"[WARN] Passed parameter {i} is not a valid parameter name. Skipping.")
            continue
        val = kwargs[i]     # Passed (param, val); we can ensure param name is correct
        corr_type = valid_keys[i]   # The type val should be
        if not isinstance(val, corr_type):
            orig_type = type(val)
            try:
                val = corr_type(val)
            except Exception as e:
                print(f"[WARN] Could not convert parameter {i} from type {orig_type} to {corr_type}. Leaving as default.")
                continue
        params_use[i] = val

    params_use["area"] = area
    params_use["status"] = status
    if point:
        params_use["point"] = point

    return _request(params_use)

def get_active_alert_count() -> Dict:
    return _request(params = {}, 
                    URL=f"{URL}/count")
