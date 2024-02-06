from fastapi import HTTPException, status

def raise_bad_request(message):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=message)