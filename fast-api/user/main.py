from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import logging  

from user_app.users import users_route

# Rest of your code
app = FastAPI(openapi_url="/api/v1/users/openapi.json", docs_url="/api/v1/users/docs")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # або "*" для дозволу всіх джерел
    allow_credentials=True,
    allow_methods=["*"],  # Дозволяє всі методи
    allow_headers=["*"],  # Дозволяє всі заголовки
)

logger = logging.getLogger(__name__)

app.include_router(users_route, prefix='/api/v1/users', tags=["users"])



@app.get("/")
def biba():
    return {"message": "Biba handler"}