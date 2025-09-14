"""
Classes for storing API URLs

Current APIs:
    FEMA_IPAWS_ARCHIVED - Archived non-weather related alerts, pulls from the FEMA's database for all EAS sent through the IPAWS system
    NWS_ACTIVE_ALERTS - Realtime weather-related alerts form the NWS
"""

####
# TODO:
#   Add valid key list
####

from datetime import datetime
from typing import Any, Dict, List


class Settings:
    class FEMA:
        IPAWS_ARCHIVED = "https://www.fema.gov/api/open/v1/IPAWSArchivedAlerts"
        # Store the valid kwargs as a dict with {name : dtype}
        VALID_SEARCH_KEYS = {"identifier": str,
                             "sender": str,
                             "sent": datetime,
                             "status": str,
                             "msgType": str,
                             "source": str,
                             "scope": str,
                             "restriction": str,
                             "addresses": str,
                             "code": List[str],
                             "note": str,
                             "searchGeometry": Dict[str, Any],
                             "cogId": int,
                             "xmlns": str,
                             "event": str,
                             "onset": datetime,
                             "expires": datetime,
                             "urgency": str,
                             "category": List[str]}
    class NWS:
        DEFAULT_HEADERS = {"User-Agent": "pyEAS/0.1",
                           "Accept": "application/geo+json"}
        ACTIVE_ALERTS = "https://api.weather.gov/alerts/active"
        # Store the valid kwargs as a dict with {name : dtype}
        VALID_SEARCH_KEYS = {"sent": datetime,
                             "effective": datetime,
                             "onset": datetime,
                             "status": str,
                             "messageType": str,
                             "category": str,
                             "severity": str,
                             "urgency": str,
                             "certainty": str,
                             "event": str,
                             "sender": str,
                             "senderName": str,
                             "headline": str,
                             "responseType": List[str],
                             "scope": str}