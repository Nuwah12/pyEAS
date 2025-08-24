from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from datetime import datetime

class NWSAlert(BaseModel):
    id: str
    source: str                      # "FEMA" or "NWS"
    sent: datetime
    effective: Optional[datetime]
    expires: Optional[datetime]
    status: Optional[str]            # e.g. "Actual"
    msg_type: Optional[str]          # e.g. "Alert", "Update"
    scope: Optional[str]             # e.g. "Public"
    category: Optional[str]          # e.g. "Met"
    event: Optional[str]             # e.g. "Tornado Warning"
    urgency: Optional[str]
    severity: Optional[str]
    certainty: Optional[str]
    headline: Optional[str]
    description: Optional[str]
    instruction: Optional[str]
    sender_name: Optional[str]
    references: Optional[List[str]]
    area: Optional[List["Area"]]     # nested model
    links: Optional[List[HttpUrl]]   # NWS API often returns links

