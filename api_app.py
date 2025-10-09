from fastapi import FastAPI
from controller.address_book_api import router as address_book_router
from controller.country_api import router as country_router

app = FastAPI()
api_app = FastAPI()

api_app.include_router(address_book_router)
api_app.include_router(country_router)

app.mount("/api/v1", api_app)