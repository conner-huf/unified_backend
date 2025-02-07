from fastapi.encoders import jsonable_encoder
from bson import ObjectId

from config import config
from data.db import red_ribbon_db as db
from models.red_ribbon.user import User
from models.red_ribbon.present import Present

class RibbonService:
    users = db.Users
    
    @staticmethod
    async def get_user_wishlist(user_id: str) -> dict:
        try:
            object_id = ObjectId(user_id)

            user = await RibbonService.users.find_one({"_id": object_id})
            if user:
                user_model = User(**user)
                return jsonable_encoder(user_model.wishlist)
            else:
                return {"error": f"user {user_id} not found"}
        except Exception as e:
            return {"error": str(e)}
    
    @staticmethod
    async def get_user_info(user_id: str) -> dict:
        try:
            object_id = ObjectId(user_id)

            user = await RibbonService.users.find_one({"_id": object_id})
            if user:
                user_model = User(**user)
                return jsonable_encoder(user_model)
            else:
                return {"error": f"user {user_id} not found"}
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    async def add_wishlist_item(user_id: str, present_data: dict) -> dict:
        try:
            object_id = ObjectId(user_id)
            user = await RibbonService.users.find_one({"_id": object_id})
            if user:
                present = Present(**present_data)
                user_model = User(**user)

                user_model.wishlist.append(present)

                update_result = await RibbonService.users.update_one(
                    {"_id": object_id}, {"$set": {"wishlist": jsonable_encoder(user_model.wishlist)}}
                )

                if update_result.modified_count == 1:
                    return {"success": f"item added to wishlist for user {user_id}"}
                else:
                    return {"error": "Failed to update wishlist"}
            else:
                return {"error": f"user {user_id} not found"}
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    async def delete_wishlist_item(user_id: str, present_id: str) -> dict:
        try:
            object_id = ObjectId(user_id)
            user = await RibbonService.users.find_one({"_id": object_id})
            if user:
                user_model = User(**user)

                user_model.wishlist = [present for present in user_model.wishlist if present.id != present_id]

                update_result = await RibbonService.users.update_one(
                    {"_id": object_id}, {"$set": {"wishlist": jsonable_encoder(user_model.wishlist)}}
                )

                if update_result.modified_count == 1:
                    return {"success": f"item with id {present_id} deleted from wishlist for user {user_id}"}
                else:
                    return {"error": "Failed to update wishlist"}
            else:
                return {"error": f"user {user_id} not found"}
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    async def update_wishlist_item(user_id: str, present_id: str) -> dict:
        try:
            object_id = ObjectId(user_id)
            user = await RibbonService.users.find_one({"_id": object_id})
            if user:
                user_model = User(**user)
            else:
                return {"error": f"user {user_id} not found"}
        except Exception as e:
            return {"error": str(e)}

    # TODO: Implement a method for creating a new gift group

    # TODO: Implement a method for fetching all members in a gift group

    # TODO: Implement a method for adding an existing user to a gift group

    # TODO: Implement a method for deleting an existing user from a gift group
