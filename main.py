from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/customers")
async def get_customers():
    return JSONResponse(status_code=200, content={"message": "OK"})

@app.get("/customers/status")
async def get_customers_status():
    return JSONResponse(status_code=200, content={"status": "up"})
