from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import resume_api, noodle_api

app = FastAPI(
  title="Unified Backend API",
  description="This a single backend API to serve all of my personal projects from one hosted location.",
  version="1.0.0",
)

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

app.include_router(resume_api.router, prefix="/resume", tags=["Resume site"])
app.include_router(noodle_api.router, prefix="/noodle", tags=["Noodle Backend"])

@app.get("/")
async def root():
  return {
    "welcome": "Welcome to the Unified Backend ConnerAPI! This API is a single location to serve all of the API needs of my personal projects.",
    "valid routes": {
      "/resume": "API for accessing my resume",
      "/noodle": "Noodle Backend",
      "/ribbon": "API for accessing gift data for users"
    }
  }