from fastapi import FastAPI

from app.api.api_v1.api import router as api_router
from mangum import Mangum

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

app.include_router(api_router, prefix="/api/v1")

# Mangum creates the handler function for AWS Lambda
handler = Mangum(app)

