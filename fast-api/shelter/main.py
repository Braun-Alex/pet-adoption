import os

from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI


from shelter import shelter_route

if __name__ == "__main__":

    app = FastAPI(openapi_url="/api/v1/shelter/openapi.json", docs_url="/api/v1/shelter/docs")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # або "*" для дозволу всіх джерел
        allow_credentials=True,
        allow_methods=["*"],  # Дозволяє всі методи
        allow_headers=["*"],  # Дозволяє всі заголовки
    )


    app.include_router(shelter_route, prefix='/api/v1/shelter', tags=["shelter"])

    @app.get("/")
    def biba():
        return {"message": "Biba handler"}
# db = SessionLocal()

# shelter_service = ShelterService(shelter_controller=ShelterController(db=db))

# Base.metadata.create_all(bind=engine)


# @app.get("/")
# def read_root():
#     return {"Hi from shelter": os.urandom(32).hex()}


# @app.post("/shelter/signup", response_model=bool)
# def register_user(shelter: ShelterLocal):
#     return shelter_service.register_shelter(shelter=shelter)


# @app.post("/shelter/login", response_model=TokenSchema)
# def authorize_user(shelter: OAuth2PasswordRequestForm = Depends()):
#     return shelter_service.authorize_shelter(shelter=shelter)


# @app.get('/shelter/profile', response_model=str)
# def get_shelter(token_payload=Depends(get_current_shelter)):
#     return shelter_service.get_shelter(token_payload.sub)
