from typing import Dict
import requests
import numpy as np
from .config import Settings
from models import NWSAlert, IPAWSAlert

def request(params: Dict, url: str) -> Dict:
    return requests.get(url, params = params).json() ## TODO: test params

def parse_nws_alerts(params: Dict) -> NWSAlert:
    resp = request(params, Settings.NWS.ACTIVE_ALERTS)

    features = resp.get("features", [])
    
    ## WARN
    if len(features) == 0:
        print("[WARN] No data for event found; continuing.")
    
    features = features[0]

    return NWSAlert(
        id = features.get("id"),
        source = "NWS",
        sent = features.get("sent"),
        effective = features.get("effective"),
        expires = features.get("ends"),
        status = features.get("status"),
        msg_type = features.get("messageType"),
        scope = features.get("scope"),
        category = features.get("cetegory"),
        event = features.get("event"),
        urgency = features.get("urgency"),
        severity = features.get("severity"),
        certainty = features.get("certainty"),
        headline = features.get("headline"),
        description = features.get("description"),
        instruction = features.get("instruction"),
        sender_name = features.get("senderName"),
        severity = features.get("severity")
    )

def parse_ipaws_alerts(params: Dict) -> IPAWSAlert:
    resp = request(params, Settings.FEMA.IPAWS_ARCHIVED)

    # Save metadata
    metadata = resp.get("metadata", [])

    features = resp.get("IpwasArchivedAlerts", [])
    
    ## WARN
    if len(features) == 0:
        print("[WARN] No data for event found; continuing.")

    features = features[0]

    return IPAWSAlert(
        id = features.get("id"),
        source = "FEMA",
        sent = features.get("sent"),
        status = features.get("status"),
        msg_type = features.get("messageType"),
        scope = features.get("scope"),
        event = features.get("event"),
        urgency = features.get("urgency"),
        severity = features.get("severity"),
        certainty = features.get("certainty"),
        headline = features.get("headline"),
        description = features.get("description"),
        instruction = features.get("instruction"),
        sender_name = features.get("senderName"),
        severity = features.get("severity")
    )