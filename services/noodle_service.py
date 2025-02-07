import base64
import requests

from config import config

class NoodleService:

  @staticmethod
  def get_ticketmaster_api_key():
    # Fetch Ticketmaster API Key from environment variables
    return config.TICKETMASTER_API_KEY
  
  @staticmethod
  def get_spotify_credentials():
    # Fetch Spotify client ID and secret from environment variables
    client_id = config.SPOTIFY_CLIENT_ID
    client_secret = config.SPOTIFY_CLIENT_SECRET
    if not client_id or not client_secret:
      raise ValueError("Spotify credentials are missing in environment variables.")
    return client_id, client_secret

  @staticmethod
  async def fetch_spotify_data(artist_name: str) -> dict:
    try:
      client_id, client_secret = NoodleService.get_spotify_credentials()

      auth_string = f"{client_id}:{client_secret}"
      auth_base64 = base64.b64encode(auth_string.encode('utf-8')).decode('utf-8')
      token_url = "https://accounts.spotify.com/api/token"
      headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded"
      }
      data = {"grant_type": "client_credentials"}
      token_response = requests.post(token_url, headers=headers, data=data)
      token_response.raise_for_status()

      token = token_response.json().get("access_token")

      if not token:
        raise ValueError("Spotify token could not be fetched.")
      
      search_url = f"https://api.spotify.com/v1/search?q={artist_name}&type=artist&limit=1"
      search_headers = {"Authorization": f"Bearer {token}"}
      search_response = requests.get(search_url, headers=search_headers)
      search_response.raise_for_status()

      result = search_response.json().get("artists", {}).get("items", [])

      if not result:
        return {"error": "No artists found"}
      return result[0]
    
    except Exception as e:
      return {"error": str(e)}
    
  @staticmethod
  async def fetch_events_by_artist(artist_name: str) -> dict:
    try:
      api_key = NoodleService.get_ticketmaster_api_key()
      url = f"https://app.ticketmaster.com/discovery/v2/events.json?apikey={api_key}&keyword={artist_name}"
      response = requests.get(url)
      response.raise_for_status()
      return response.json().get('_embedded', {}).get('events', [])
    except Exception as e:
      return {"error": str(e)}

  @staticmethod
  async def fetch_events_by_zip(zip_code: str) -> dict:
    try:
      api_key = NoodleService.get_ticketmaster_api_key()
      url = f"https://app.ticketmaster.com/discovery/v2/events.json?apikey={api_key}&postalCode={zip_code}&radius=25&unit=miles"
      response = requests.get(url)
      response.raise_for_status()
      return response.json().get('_embedded', {}).get('events', [])
    except Exception as e:
      return {"error": str(e)}

  @staticmethod
  async def fetch_events_by_city(city: str) -> dict:
    try:
      api_key = NoodleService.get_ticketmaster_api_key()
      url = f"https://app.ticketmaster.com/discovery/v2/events.json?classificationName=music&apikey={api_key}&city={city}&radius=50&unit=miles"
      response = requests.get(url)
      response.raise_for_status()
      return response.json().get('_embedded', {}).get('events', [])
    except Exception as e:
      return {"error": str(e)}