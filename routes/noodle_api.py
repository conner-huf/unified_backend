from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from services.noodle_service import NoodleService

router = APIRouter()

@router.get("/", response_model=dict)
def welcome():
  return {
    "welcome": "Welcome to the Noodle Backend API. This API is for fetching data from the Noodle Backend. Accessing this API requires a Spotify API key and a Ticketmaster API key.",
    "valid routes": {
      "/spotify_data/{artist_name}": "Get Spotify data for an artist",
      "/concert_data_artist/{artist_name}": "Get concert data for an artist",
      "/concert_data_zip/{zip_code}": "Get concert data for a zip code",
      "/concert_data_city/{city}": "Get concert data for a city"
    }
  }
  
@router.get("/spotify_data/{artist_name}")
async def get_spotify_data(artist_name: str):
  data = await NoodleService.fetch_spotify_data(artist_name)
  if "error" in data:
    raise HTTPException(status_code=404, detail=data["error"])
  return JSONResponse(content=data)

@router.get("/concert_data_artist/{artist_name}")
async def get_concert_data_by_artist(artist_name: str):
  data = await NoodleService.fetch_events_by_artist(artist_name)
  return JSONResponse(content=data)

@router.get("/concert_data_zip/{zip_code}")
async def get_concert_data_by_zip(zip_code: str):
  data = await NoodleService.zip(zip_code)
  return JSONResponse(content=data)

@router.get("/concert_data_city/{city}")
async def get_events_by_city(city: str):
  data = await NoodleService.fetch_events_by_artist(city)
  return JSONResponse(content=data)