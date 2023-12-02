from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import logging  

from application_app.application import application_router

# Rest of your code
app = FastAPI(openapi_url="/api/v1/applications/openapi.json", docs_url="/api/v1/applications/docs")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # або "*" для дозволу всіх джерел
    allow_credentials=True,
    allow_methods=["*"],  # Дозволяє всі методи
    allow_headers=["*"],  # Дозволяє всі заголовки
)

logger = logging.getLogger(__name__)

app.include_router(application_router, prefix='/api/v1/applications', tags=["applications"])



@app.get("/")
def biba():
    return {"message": "applications handler"}