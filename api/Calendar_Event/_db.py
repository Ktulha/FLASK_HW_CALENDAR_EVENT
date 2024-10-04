from model.calendar_event import CalendarEvent
from api.Calendar_Event.storage import CalendarEventStorage


class DBException(Exception):
    """Base class for database exceptions."""
    pass

class DB_Calendar_Event:
    """
    A class responsible for interacting with the calendar event database.

    It provides methods for creating, reading, listing, updating, and deleting calendar events.
    All database operations are wrapped in try-except blocks to handle potential exceptions.

    Attributes:
        _storage (CalendarEventStorage): An instance of the CalendarEventStorage class.

    Methods:
        _create(_event: CalendarEvent) -> str:
            Creates a new calendar event in the database.

        _read(_id: str) -> CalendarEvent:
            Retrieves a calendar event from the database by its ID.

        _list() -> list[CalendarEvent]:
            Retrieves a list of all calendar events from the database.

        _update(_id: str, _event: CalendarEvent):
            Updates a calendar event in the database.

        _delete(_id: str):
            Deletes a calendar event from the database.

    Raises:
        DBException: If any database operation fails.
    """
    def  __init__(self):
        self._storage=CalendarEventStorage()
    def _create(self,_event:CalendarEvent) -> str:
        try:
            return self._storage._create(_event)
        except Exception as e:
            raise DBException(f"Error creating event: {e}") from e
    def _read(self,_id:str)->CalendarEvent:
        try:
            return self._storage._read(_id)
        except  Exception as e:
            raise DBException(f"Error reading event: {e}") from e
        
    def _list(self)->list[CalendarEvent]:
        try:
            return  self._storage._list()
        except   Exception as e:
            raise  DBException(f"Error listing events: {e}") from e
    
    def _update(self,_id:str,_event:CalendarEvent):
        try:
            return self._storage._update(_id,_event)
        except  Exception as e:
            raise DBException(f"Error updating event: {e}") from e
    
    def _delete(self,_id:str):
        try:
            return self._storage._delete(_id)
        except   Exception as e:
            raise   DBException(f"Error deleting event: {e}") from e
    





