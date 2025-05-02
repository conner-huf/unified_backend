from config import config
import requests
from polygon import RESTClient

class EconomicService:
    API_KEY = config.FRED_API_KEY
    PRODUCT_URL = "https://api.stlouisfed.org/fred/series/search"
    OBSERVATIONS_URL = "https://api.stlouisfed.org/fred/series/observations"
    PolygonClient = RESTClient(config.POLYGON_API_KEY)

    @staticmethod
    def get_product_data(term: str) -> dict:
        try:
            params = {
                "search_text": term,
                "api_key": EconomicService.API_KEY,
                "file_type": "json",
                "limit": 1,
            }

            response = requests.get(EconomicService.PRODUCT_URL, params=params)
            response.raise_for_status()

            return response.json()
        except Exception as e:
            return { "error": str(e) }
        
    @staticmethod
    def get_price_observations(series_id: str) -> dict:
        try:
            params = {
                "series_id": series_id,
                "api_key": EconomicService.API_KEY,
                "file_type": "json",
            }
            response = requests.get(EconomicService.OBSERVATIONS_URL, params=params)
            response.raise_for_status()

            return response.json()
        except Exception as e:
            return { "error": str(e) }
        
    @staticmethod
    def get_USDIndex():
        try:
            response = EconomicService.PolygonClient.get_ticker_details("")
            if response is None:
                raise RuntimeError("Failed to fetch USD Index data.")
            return response
        except Exception as e:
            return { "error": str(e) }