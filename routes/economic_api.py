from fastapi import APIRouter, HTTPException, Query
from services.economic_service import EconomicService
from datetime import date

router = APIRouter()

@router.get("/", response_model=dict)
def welcome():
  return {
    "welcome": "Welcome to the Economic API. This API allows you to fetch data on the current and historic prices of common household goods.",
    "valid routes": {
      "product/{term}": "Get historical prices of a good.",
      }
  }

@router.get("/product/{term}", response_model=dict)
def get_product_data(term: str):
  try:
    product_data = EconomicService.get_product_data(term)
    if "error" in product_data:
      raise HTTPException(status_code=500, detail=product_data["error"])
    
    series_id = product_data.get("seriess", [{}])[0].get("id", None)
    if not series_id:
      raise HTTPException(status_code=404, detail="Series ID not found for the given product.")

    price_observations = EconomicService.get_price_observations(series_id)
    if "error" in price_observations:
      raise HTTPException(status_code=500, detail=price_observations["error"])

    return {
      "product": term,
      "historical_data": product_data,
      "price_observations": price_observations  
    }
  except RuntimeError as e:
    raise HTTPException(status_code=500, detail=f"Service error: {str(e)}")
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Unexpected server error: {str(e)}")