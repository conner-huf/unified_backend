from pydantic import BaseModel, Field
from datetime import date
from bson import ObjectId

class Present(BaseModel):
    id: str = Field(default_factory=lambda: str(ObjectId()))
    title: str
    price: float
    date_requested: date
    is_purchased: bool
    url: str