
from fastapi import FastAPI
import auth, database, models
from fastapi.middleware.cors import CORSMiddleware
#create DB tables
models.Base.metadata.create_all(bind=database.engine)

app=FastAPI(title="Authentication System, version=1.0.0")
#CORS config
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], #replace with domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)
#include auth routes
app.include_router(auth.router)
