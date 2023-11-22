from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import logging  

from animal_app.animals import animals_router

# Rest of your code
app = FastAPI(openapi_url="/api/v1/animals/openapi.json", docs_url="/api/v1/animals/docs")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # або "*" для дозволу всіх джерел
    allow_credentials=True,
    allow_methods=["*"],  # Дозволяє всі методи
    allow_headers=["*"],  # Дозволяє всі заголовки
)

logger = logging.getLogger(__name__)

app.include_router(animals_router, prefix='/api/v1/animals', tags=["animals"])



@app.get("/")
def biba():
    return {"message": "Animal handler"}