import validators

from fastapi import FastAPI

from schemas import URLBaseModel, URLInfo, URL
from helpers import raise_bad_request

app = FastAPI()

@app.get('/')
def read_root():
    """
    ROUTE_NAME: /
    
    REQUEST BODY: None \n
    RESPONSE: Simple String with a little introductory info
    """
    return "Welcome to URL Shortener"

@app.post('/url')
def create_url(url: URLBaseModel):
    if not validators.url(url.target_url):
        raise_bad_request(message="Your provided URL is not valid")
        
    return f"TODO: Create database entry for: {url.target_url}"