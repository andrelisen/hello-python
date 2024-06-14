from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/customers")
async def get_customers():
    return JSONResponse(status_code=200, content={"message": "Customers OK"})

@app.get("/customers/health")
async def get_customers_health():
    return JSONResponse(status_code=200, content={"status": "up"})
