import secrets
import validators

from fastapi import FastAPI, Depends, HTTPException

from sqlalchemy.orm import Session 

from schemas import URLBaseModel, URLInfo, URL
from . import models
from database import SessionLocal, engine
from helpers import raise_bad_request

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# db conf
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# API Endpoints
@app.get('/')
def read_root():
    """
    ROUTE_NAME: /
    
    REQUEST BODY: None \n
    RESPONSE: Simple String with a little introductory info
    """
    return "Welcome to URL Shortener"


@app.post('/url', response_model=URLInfo)
def create_url(url: URLBaseModel, db: Session = Depends(get_db)):
    """
    ROUTE_NAME: /url
    
    REQUEST BODY: { "target_url": "https://google.com" } \n
    RESPONSE: Success response with Shortened url details
    """
    if not validators.url(url.target_url):
        raise_bad_request(message="Your provided URL is not valid")
        
    chars = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
    key = "".join(secrets.choice(chars) for _ in range(5))
    secret_key = "".join(secrets.choice(chars) for _ in range(8))
    
    db_url = models.URL(
        target_url=url.target_url,
        key=key,
        secret_key=secret_key
    )
    
    db.add(db_url)
    db.commit()
    
    db.refresh(db_url)
    db_url.url = key
    db_url.admin_url = secret_key
        
    return db_url