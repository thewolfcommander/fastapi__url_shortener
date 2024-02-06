from datetime import datetime

from sqlalchemy import Boolean, Column, Integer, String, DateTime

from .database import Base

class URL(Base):
    __tablename__ = 'urls'
    
    id = Column(Integer, primary_key=True)
    key = Column(String, unique=True, index=True)
    secret_key = Column(String, unique=True, index=True)
    target_url = Column(String, index=True)
    is_active = Column(Boolean, default=True)
    clicks = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)