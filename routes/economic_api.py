from fastapi import APIRouter, HTTPException
from services.economic_service import EconomicService

router = APIRouter()

@router.get("/", response_model=dict)
def welcome():
  return {
    "welcome": "Welcome to the Stocks API. This API allows you to fetch stock market data.",
    "valid routes": {
      "/price/{ticker}": "Get the latest price of a stock",
      "/historical/{ticker}": "Get historical data of a stock",
      "/company/{ticker}": "Get company information",
    }
  }

@router.get("/price/{ticker}", response_model=dict)
def get_stock_price(ticker: str):
  try:
    price = EconomicService.get_stock_price(ticker)
    return {"ticker": ticker, "price": price}
  except RuntimeError as e:
    raise HTTPException(status_code=500, detail=f"Service error: {str(e)}")
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Unexpected server error: {str(e)}")

@router.get("/historical/{ticker}", response_model=dict)
def get_historical_data(ticker: str):
  try:
    historical_data = EconomicService.get_historical_data(ticker)
    return {"ticker": ticker, "historical_data": historical_data}
  except RuntimeError as e:
    raise HTTPException(status_code=500, detail=f"Service error: {str(e)}")
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Unexpected server error: {str(e)}")

@router.get("/company/{ticker}", response_model=dict)
def get_company_information(ticker: str):
  try:
    company_info = EconomicService.get_company_information(ticker)
    return {"ticker": ticker, "company_info": company_info}
  except RuntimeError as e:
    raise HTTPException(status_code=500, detail=f"Service error: {str(e)}")
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Unexpected server error: {str(e)}")