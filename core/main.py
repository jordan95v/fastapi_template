from fastapi import FastAPI, Request

__all__: list[str] = ["app"]

app: FastAPI = FastAPI()


@app.get("/healthcheck", tags=["healthcheck"])
def health_check(request: Request) -> dict[str, str]:
    """This endpoint is used to verify that the server is up.

    Args:
        request : The incoming HTTP request.

    Returns:
        A response with a status code of 200 and a JSON indicating the server status.
    """

    return dict(status="Server is up")
