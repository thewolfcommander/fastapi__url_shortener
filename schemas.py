from pydantic import BaseModel
from datetime import datetime

class URLBaseModel(BaseModel):
    target_url: str
    

class URL(URLBaseModel):
    is_active: bool
    clicks: int
    
    class Config:
        orm_mode = True
        
    
class URLInfo(URL):
    url: str
    admin_url: str
    created_at: datetime
    updated_at: datetime
    
