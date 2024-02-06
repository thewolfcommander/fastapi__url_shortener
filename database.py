from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import get_settings

# defining engine
engine = create_engine(url=get_settings().db_url, connect_args={ 'check_same_thread': False })

SessionLocal = sessionmaker(auto_commit=False, auto_flush=False, bind=engine)

Base = declarative_base()