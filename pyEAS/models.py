from pydantic import BaseModel, HttpUrl
from typing import List, Optional
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

