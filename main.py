from fastapi import FastAPI
from routes.route import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Adjust for your frontend's
    allow_methods=["*"],
    allow_headers=["*"],
)
