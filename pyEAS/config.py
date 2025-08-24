"""
Classes for storing API URLs

Current APIs:
    FEMA_IPAWS_ARCHIVED - Archived non-weather related alerts, pulls from the FEMA's database for all EAS sent through the IPAWS system
    NWS_ACTIVE_ALERTS - Realtime weather-related alerts form the NWS
"""

class Settings:
    class FEMA:
        IPAWS_ARCHIVED = "https://www.fema.gov/api/open/v1/IPAWSArchivedAlerts"
    class NWS:
        ACTIVE_ALERTS = "https://api.weather.gov/alerts/active"