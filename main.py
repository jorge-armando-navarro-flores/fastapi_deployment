import os
from fastapi import FastAPI, Header, HTTPException, Depends

app = FastAPI()

API_KEY = os.getenv("API_KEY", "default-dev-key")  # fallback for local dev

def verify_api_key(x_api_key: str = Header(default=None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

@app.get("/")
def read_root():
    return {"message": "Public endpoint - no auth needed"}

@app.post("/data", dependencies=[Depends(verify_api_key)])
def receive_data(payload: dict):
    return {"received": payload}
