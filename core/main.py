from contextlib import asynccontextmanager
from fastapi import FastAPI, Request

from core.config import ENGINE
from core.models.base import Base

__all__: list[str] = ["app"]


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(ENGINE)
    yield


app: FastAPI = FastAPI(lifespan=lifespan)


@app.get("/health_check", tags=["healthcheck"])
def health_check(request: Request) -> dict[str, str]:
    """Health check endpoint. This endpoint is used to verify that the server is up.

    Args:
        request : The incoming HTTP request.

    Returns:
        A response with a status code of 200 and a JSON indicating the server status.
    """

    return dict(status="Server is up")
