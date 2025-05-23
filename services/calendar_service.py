import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from pydantic import BaseModel

# The email of the calendar owner (example@gmail.com)
CALENDAR_ID = os.getenv("GOOGLE_CALENDAR_ID", "example@gmail.com")
SERVICE_ACCOUNT_FILE = os.getenv("GOOGLE_SERVICE_ACCOUNT_FILE", "service_account.json")

class AppointmentRequest(BaseModel):
    name: str
    email: str
    start_time: str
    end_time: str
    description: str = ""

class CalendarService:
    @staticmethod
    async def create_event(appointment: AppointmentRequest):
        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE,
            scopes=['https://www.googleapis.com/auth/calendar']
        )

        service = build('calendar', 'v3', credentials=credentials)

        event = {
            'summary': f"Appointment with {appointment.name}",
            'description': appointment.description,
            'start': {
                'dateTime': appointment.start_time,
                'timeZone': 'UTC',
            },
            'end': {
                'dateTime': appointment.end_time,
                'timeZone': 'UTC',
            },
            'attendees': [
                {'email': appointment.email},
            ],
        }

        created_event = service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
        return created_event