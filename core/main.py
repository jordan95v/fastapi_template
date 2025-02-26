from contextlib import asynccontextmanager
from typing import AsyncGenerator
from fastapi import FastAPI, Request

from core.config import ENGINE
from core.models.base import Base

__all__: list[str] = ["app"]


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Lifespan context manager for the FastAPI application.

    This context manager is used to manage the lifespan of the FastAPI application.
    It creates all the database tables defined in the Base metadata using the ENGINE
    before yielding control back to the application.

    Args:
        app: The FastAPI application instance.
    """

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
