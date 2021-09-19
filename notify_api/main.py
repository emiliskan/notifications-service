import logging

import uvicorn
from celery import Celery
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api.v1 import notifier
from core import config
from core.logger import LOGGING
from db import celery_app

app = FastAPI(
    title=config.PROJECT_NAME,
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
)


@app.on_event("startup")
async def startup():
    celery_app.app = Celery("senders", broker=config.CELERY_BROKER_URL)


app.include_router(notifier.router, prefix="/v1", tags=["Notifier"])


@app.on_event("shutdown")
async def shutdown():
    pass

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        log_config=LOGGING,
        log_level=logging.DEBUG,
        reload=True
    )
