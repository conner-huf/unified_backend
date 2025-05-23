from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from services.calendar_service import CalendarService

router = APIRouter()

class AppointmentRequest(BaseModel):
    name: str
    email: str
    start_time: str  # ISO 8601 format
    end_time: str    # ISO 8601 format
    description: str = ""

@router.post("/book", status_code=201)
async def book_appointment(appointment: AppointmentRequest):
    try:
        event = await CalendarService.create_event(appointment)
        return {"success": True, "event": event}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Booking failed: {e}")