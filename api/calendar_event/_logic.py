from api.calendar_event._db import Calendar_Events_DB
from model.calendar_event import Calendar_Event

TOPIC_LIMIT=30
CONTENT_LIMIT=200

class LogicException(Exception):
  pass

class Calendar_Events_Logic:
  def  __init__(self):
    self._db=Calendar_Events_DB()
  
  def _create(self,_event:Calendar_Event)->str:
    print("create")
    try:      
      return  self._db._create(_event)
    except  Exception as ex:
      raise  LogicException(f"Error creating event: {ex}")
    
  def _read(self, _id: str) -> Calendar_Event:
    try:
      return self._db._read(_id)
    except Exception as ex:
      raise LogicException(f"Error reading event: {ex}")
  def _list(self)->list[Calendar_Event]:
    try:
      return self._db._list()
    except Exception as ex:
      raise LogicException(f"Error listing events: {ex}")
  def  _update(self,_id:str,_event:Calendar_Event):
    try:
      return  self._db._update(_id,_event)
    except Exception as ex:
      raise LogicException(f"Error updating event: {ex}")
  def _delete(self, _id: str):
    try:
      return self._db._delete(_id)
    except Exception as ex:
      raise LogicException(f"Error deleting event: {ex}")
    

    

  
  


