from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from services.ribbon_service import RibbonService

router = APIRouter()

@router.get("/", response_model=dict)
def welcome():
  return {
    "welcome": "Welcome to the Red Ribbon Backend API. This API is for fetching data from the ribbon backend. This backend accesses data on users and the gifts they want.",
    "valid routes": {
      "/user/{user_id}": "Get info for a user by user_id (test user = 6776c071bb7f0ba5bd3732ff)",
      "/user/{user_id}/wishlist": "Get wishlist for a user by user_id (test user = 6776c071bb7f0ba5bd3732ff)"
    }
  }

@router.get("/user/{user_id}")
async def get_user_info(user_id: str):
  data = await RibbonService.get_user_info(user_id)
  if "error" in data:
    raise HTTPException(status_code=404, detail=data["error"])
  return JSONResponse(content=data)

@router.get("/user/{user_id}/wishlist")
async def get_wishlist(user_id: str):
  data = await RibbonService.get_user_wishlist(user_id)
  if "error" in data:
    raise HTTPException(status_code=404, detail=data["error"])
  return JSONResponse(content=data)

@router.post("/user/{user_id}/wishlist")
async def add_wishlist_item(user_id: str, present_data: dict):
  data = await RibbonService.add_wishlist_item(user_id, present_data)
  if "error" in data:
    raise HTTPException(status_code=404, detail=data["error"])
  return JSONResponse(content=data)

@router.put("/user/{user_id}/wishlist/{present_id}")
async def update_wishlist_item(user_id: str, present_id: str):
  data = await RibbonService.update_wishlist_item(user_id, present_id)
  if "error" in data:
    raise HTTPException(status_code=404, detail=data["error"])
  return JSONResponse(content=data)

@router.delete("/user/{user_id}/wishlist/{present_id}")
async def delete_wishlist_item(user_id: str, present_id: str):
  data = await RibbonService.delete_wishlist_item(user_id, present_id)
  if "error" in data:
    raise HTTPException(status_code=404, detail=data["error"])
  return JSONResponse(content=data)

# TODO: Implement a route for creating a new gift group

# TODO: Implement a route for fetching all members in a gift group

# TODO: Implement a route for adding an existing user to a gift group

# TODO: Implement a route for deleting an existing user from a gift group