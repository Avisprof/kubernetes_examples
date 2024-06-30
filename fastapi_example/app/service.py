from fastapi import FastAPI
from loguru import logger
import time

app = FastAPI(openapi_prefix="/server")

@app.get("/")
async def check():
    return {"status": "ok"}

@app.get("/predict")
async def predict():
    logger.info("Start prediction...")
    time.sleep(10)
    logger.info("Finish prediction")
    return {"status": "ok",
            "result": 555}


