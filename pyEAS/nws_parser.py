from typing import Dict
import requests
import numpy as np
from .config import *
from models import *

def request(params: Dict) -> Dict:
    return requests.get(Settings.NWS.ACTIVE_ALERTS,
                        params = params).json()

def parse_nws_alerts(params: Dict) -> NWSAlert:
    resp = request(params)

    features = resp.get("features", [])
    
    ## WARN
    if len(features) == 0:
        print("[WARN] No data for event found; continuing.")
    
