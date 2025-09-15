
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

def _filter_response(response: Dict, filter_params: Dict) -> Dict:
    return {k: v for k, v in response.items()
            if k not in filter_params or v in filter_params[k]}

def get_active_alerts(
    area: str = "PA", # Default to PA
    status: str = "actual",
    point: Optional[tuple[str, str]] = None,
    message_type: Optional[str] = None,
    event: Optional[str] = None,
    code: Optional[str] = None,
    region_type: Optional[str] = None,
    zone: Optional[str] = None,
    urgency: Optional[str] = None,
    severity: Optional[str] = None,
    certainty: Optional[str] = None,
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
    ###         1. Arguments passed via URL (will be function args)
    ###         2. Arguments that require filterting of response (kwargs)
    ### Obviously these have to be trated differently, but it'd be good for the user to be able to treat them  the same 
    valid_keys = Settings.NWS.VALID_SEARCH_KEYS
    url_params = {"area": area, "status": status}
    filter_params = {}
    # Check for positional args, they are typed so we can just append them to a list of they were passed (i.e. not None)
    for var in ["point", "message_type", "event", "code", 
                "region_type", "zone", "urgency", "severity", "certainty"]:
        value = locals()[var]
        if value:
            url_params[var] = value
    # Now check kwargs, must verify name and type
    for i in kwargs:
        if i not in valid_keys.keys():
            print(f"[WARN] Keyword argument {i} not valid; continuing.")
            continue

        if not isinstance(kwargs[i], valid_keys[i]):
            print(f"[WARN] type of keyword argument {i} passed was {type(kwargs[i])}, but requires type {valid_keys[i]}")
            continue
        
        filter_params[i] = kwargs[i]
        
    resp = _request(url_params).get("features")[0]

    return _filter_response(resp, filter_params)

def get_active_alert_count() -> Dict:
    return _request(params = {}, 
                    URL=f"{URL}/count")
