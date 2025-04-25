from fastapi import FastAPI, Header, HTTPException, Depends

app = FastAPI()

API_KEY = "apikey"

# Dependency for protecting POST endpoint
def verify_api_key(x_api_key: str = Header(default=None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

# Public GET route
@app.get("/")
def read_root():
    return {"message": "Public endpoint - no auth needed"}

# Protected POST route
@app.post("/data", dependencies=[Depends(verify_api_key)])
def receive_data(payload: dict):
    return {"received": payload}
