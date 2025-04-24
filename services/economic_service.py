import requests
from config import config

class EconomicService:
    BASE_URL = "https://api.polygon.io"
    API_KEY = config.POLYGON_API_KEY 

    @staticmethod
    def get_stock_price(ticker: str) -> dict:
        try:
            url = f"{EconomicService.BASE_URL}/v2/snapshot/locale/us/markets/stocks/tickers/{ticker}"
            params = {"apiKey": EconomicService.API_KEY}
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            return data.get("results", {})
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def get_historical_data(ticker: str) -> dict:
        try:
            url = f"{EconomicService.BASE_URL}/v2/aggs/ticker/{ticker}/range/1/day/2023-01-01/2023-12-31"
            params = {"apiKey": EconomicService.API_KEY}
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            return data.get("results", [])
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def get_company_information(ticker: str) -> dict:
        try:
            url = f"{EconomicService.BASE_URL}/v3/reference/tickers/{ticker}"
            params = {"apiKey": EconomicService.API_KEY}
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            return data.get("results", {})
        except Exception as e:
            return {"error": str(e)}