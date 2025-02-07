from pydantic import BaseModel
from typing import List
from models.red_ribbon.present import Present

class User(BaseModel):
    first_name: str
    last_name: str
    email: str
    wishlist: List[Present]
