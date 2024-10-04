from model.calendar_event import CalendarEvent
from api.Calendar_Event.storage import CalendarEventStorage


class DBException(Exception):
    """Base class for database exceptions."""
    pass

class DB_Calendar_Event:
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
    





