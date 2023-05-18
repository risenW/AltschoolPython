from fastapi import FastAPI
from router.accounts import accounts_router
from router.users import users_router

import sentry_sdk


sentry_sdk.init(
    dsn="https://eafce32009ca4105b59fe7c0a323614f@o4505201232904192.ingest.sentry.io/4505204931166208",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production,
    traces_sample_rate=1.0,
)

app = FastAPI()

app.include_router(
    accounts_router,
    prefix="/accounts",
    tags=["Account"],
)

app.include_router(
    users_router,
    prefix="/users",
    tags=["User"],
)


@app.get("/")
def home():
    return "Welcome to my Fish Banking API v1.0"
