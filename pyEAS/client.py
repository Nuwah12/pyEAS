from .api import fema, nws

class EASClient:
    def __init__(self, api: str, timeout: int = 15):
        self.api = self.api
        self.timeout = timeout
    
    def get_active_alerts(self, **filters):
        """
        Get the active alerts (weather only)
        """