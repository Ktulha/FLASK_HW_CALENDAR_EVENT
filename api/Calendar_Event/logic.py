from api.Calendar_Event._db import DB_Calendar_Event
from model.calendar_event import CalendarEvent



class LogicError(Exception):
    pass

class CalendarEventLogic:
    def __init__(self) -> None:
        self._db=DB_Calendar_Event()
    def _create(self,_event:CalendarEvent)->str:
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
        try:
            return  self._db._update(_id,_event)
        except Exception  as e:
            raise LogicError(f"Error updating calendar event: {e}") from e
    
    def _delete(self,_id:str):
        try:
            return self._db._delete(_id)
        except  Exception  as e:
            raise LogicError(f"Error deleting calendar event: {e}") from e
        

    

