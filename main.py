from fastapi import FastAPI
from routes.route import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust for your frontend's
    allow_methods=["*"],
    allow_headers=["*"],
)
