from fastapi import FastAPI
from schema import Response
from api.api import api_router

app = FastAPI(
    title="Books API",
    description="A simple API to manage books in a library",
    version="1.0.0",
    docs_url="/api/v1/docs",
)

app.include_router(api_router, prefix="/api/v1")


@app.get("/", status_code=200)
def home():
    return Response(message="Hello from the books API")
