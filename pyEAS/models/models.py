from pydantic import BaseModel, HttpUrl
from typing import List, Literal, Optional
from datetime import datetime

class NWSAlert(BaseModel):
    id: str
    source: str # "NWS"
    sent: datetime
    effective: Optional[datetime]
    expires: Optional[datetime]
    status: Optional[str]      
    msg_type: Optional[str]    
    scope: Optional[str]     
    category: Optional[str]        
    event: Optional[str]            
    urgency: Optional[str]
    severity: Optional[str]
    certainty: Optional[str]
    headline: Optional[str]
    description: Optional[str]
    instruction: Optional[str]
    sender_name: Optional[str]

class IPAWSAlert(BaseModel):
    id: str
    source: str # "FEMA"
    identifier: str
    sent: datetime
    status: Optional[str]
    msg_type: Optional[str]
    scope: Optional[str]
    event: Optional[str]
    onset: Optional[datetime]
    expires: Optional[datetime]
    urgency: Optional[str]
    headline: Optional[str]
    severity: Optional[str]
    certainty: Optional[str]
    sender_name: Optional[str]

### The NWS API offers distinct parameters for each field
class NWSAPIParams(BaseModel):
    area: str
    point: Optional[tuple[str, str]]
    status: Optional[Literal["actual", "exercise", "system", "test", "draft"]]
    message_type: Optional[Literal["alert", "update", "cancel"]]
    urgency: Optional[Literal["immediate", "expected", "future", "past", "unknown"]]
    severity: Optional[Literal["extreme", "severe", "moderate", "minor", "unknown"]]
    certainty: Optional[Literal["observed", "likely", "possible", "unlikely", "unknown"]]

### The FEMA API has all field values be passed via a filter variable
class FEMAParams(BaseModel):
    event: str
    sent: datetime
    sent_date_end: Optional[datetime]

