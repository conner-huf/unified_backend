from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from services.economic_service import EconomicService

router = APIRouter()

@router.get("/", response_model=dict)
def welcome():
  return {
    "welcome": "Welcome to the Economy Tracker API. This API is for fetching data related to the economic performance of the U.S. This backend accesses data on users and the gifts they want.",
    "valid routes": {
      "/stocks": "",
    }
  }