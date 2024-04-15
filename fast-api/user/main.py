from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from user_app.models.user_local_model import TokenSchema
from typing import Optional
from user_app.dependencies.dependencies import refresh_access_token

import logging

from user_app.users import users_route

app = FastAPI(openapi_url="/api/v1/users/openapi.json", docs_url="/api/v1/users/docs")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

logger = logging.getLogger(__name__)

logger.info("INFO")
logger.debug("DEBUG")
logger.warn("WARN")
logger.error("ERROR")

app.include_router(users_route, prefix='/api/v1/users', tags=["users"])

@app.get("/")
def biba():
    return {"message": "Biba handler"}

@app.get("/api/v1/token/refresh", response_model=Optional[TokenSchema])
def refresh_token(tokens: TokenSchema = Depends(refresh_access_token)):
    return tokens


