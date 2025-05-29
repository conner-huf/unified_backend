import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build
from pydantic import BaseModel

email_account = "example@gmail.com"
CALENDAR_ID = os.getenv("GOOGLE_CALENDAR_ID", email_account)
service_account_info = json.loads(os.environ["GOOGLE_SERVICE_ACCOUNT_JSON"])


class AppointmentRequest(BaseModel):
    name: str
    email: str
    start_time: str
    end_time: str
    description: str = ""

class CalendarService:
    @staticmethod
    async def create_event(appointment: AppointmentRequest):
        credentials = service_account.Credentials.from_service_account_info(
            service_account_info,
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
        }

        created_event = service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
        return created_event