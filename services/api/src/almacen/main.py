from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from time import sleep

import uvicorn
from fastapi import FastAPI
from fastapi.logger import logger

from almacen.config import app_config
from almacen.endpoints import productos


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncGenerator:
    logger.info("Starting FastAPI server...")
    yield
    sleep(5)
    logger.info("FastAPI server finished!")


app = FastAPI(docs_url="/", lifespan=lifespan, root_path=app_config.BASE_URL)
app.include_router(productos.router, tags=["productos"], prefix="/productos")

if __name__ == "__main__":
    uvicorn.run("app:app", port=8080, reload=True, host="0.0.0.0", log_level="info")
