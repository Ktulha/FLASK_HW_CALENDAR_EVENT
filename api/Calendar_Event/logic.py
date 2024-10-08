"""
This module defines constants used for validating calendar event properties.

These constants set limits on the topic length, content length, and the expected date format for calendar events, ensuring that events adhere to specific criteria for proper handling and storage.

Constants:
    TOPIC_LIMIT (int): The maximum allowed length for the topic of a calendar event.
    CONTENT_LIMIT (int): The maximum allowed length for the content of a calendar event.
    DATE_FORMAT (str): The expected date format for calendar events.

Class:
    LogicError(Exception): A custom exception class for logic errors.

Class:
    CalendarEventLogic:
        A class that provides methods for creating, reading, listing, updating, and deleting calendar events.

        Attributes:
            _db (DB_Calendar_Event): An instance of the DB_Calendar_Event class, used for database operations.

        Methods:
            __init__() -> None: Initializes the CalendarEventLogic instance with a DB_Calendar_Event instance.

            _validate_event(_event: CalendarEvent) -> None: Validates a calendar event, checking its topic, content, and date format.

            _create(_event: CalendarEvent) -> str: Creates a new calendar event and returns its ID.

            _read(_id: str) -> CalendarEvent: Retrieves a calendar event by its ID.

            _list() -> list[CalendarEvent]: Retrieves a list of all calendar events.

            _update(_id: str, _event: CalendarEvent) -> str: Updates an existing calendar event and returns its ID.

            _delete(_id: str) -> None: Deletes a calendar event by its ID.
"""
from api.Calendar_Event._db import DB_Calendar_Event
from model.calendar_event import CalendarEvent
from datetime  import datetime

TOPIC_LIMIT=30
CONTENT_LIMIT=200
DATE_FORMAT="%Y-%m-%d"

class LogicError(Exception):
    pass

class CalendarEventLogic:
    def __init__(self) -> None:
        self._db=DB_Calendar_Event()
        
    def _validate_event(self,_event:CalendarEvent):
        if not isinstance(_event,CalendarEvent):
            raise LogicError("Invalid event")
        if _event.topic is None or len(_event.topic)>TOPIC_LIMIT:
            raise LogicError(
                f"Invalid topic length.  Topic must be between 1 and {str(TOPIC_LIMIT)} characters"
            )
        if _event.content is None or len(_event.content)>CONTENT_LIMIT:
            raise  LogicError(
                f"Invalid content length.  Content must be between 1 and {str(CONTENT_LIMIT
                )} characters"
                )
        try:
            datetime.strptime(_event.date,DATE_FORMAT)
        except ValueError as e:
            raise LogicError(
                f"Invalid date format.  Date must be in {DATE_FORMAT} format"
            ) from e


    def _create(self,_event:CalendarEvent)->str:
        self._validate_event(_event)
        try:
            return self._db._create(_event)
        except Exception  as e:
            raise LogicError(f"Error creating calendar event: {e}") from e
    def _read(self,_id:str)->CalendarEvent:
        try:
            return self._db._read(_id)
        except Exception  as e:
            raise LogicError(f"Error reading calendar event: {e}") from e
    def _list(self)->list[CalendarEvent]:
        try:
            return self._db._list()
        except Exception  as e:
            raise LogicError(f"Error listing calendar events: {e}") from e
    
    def _update(self,_id:str,_event:CalendarEvent)->str:
        self._validate_event(_event)
        try:
            return  self._db._update(_id,_event)
        except Exception  as e:
            raise LogicError(f"Error updating calendar event: {e}") from e
    
    def _delete(self,_id:str):
        try:
            return self._db._delete(_id)
        except  Exception  as e:
            raise LogicError(f"Error deleting calendar event: {e}") from e
        

    

