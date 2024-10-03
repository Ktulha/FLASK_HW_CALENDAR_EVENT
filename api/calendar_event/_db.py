from api.calendar_event._storage import Calendar_Events_Storage
from model.calendar_event import Calendar_Event

class DB_Exception(Exception):
  pass

class Calendar_Events_DB:
  def __init__(self):
    self._storage=Calendar_Events_Storage
  
  def _create(self,_event:Calendar_Event)->str:
    try:
      return self._storage._create(_event)
    except Exception as ex:
      raise  DB_Exception(f"Error creating event: {ex}")
  def _read(self,_id:str)->Calendar_Event:
    try:
      return self._storage._read(_id)
    except Exception as ex:
      raise   DB_Exception(f"Error reading event: {ex}")
  def _list(self)->list[Calendar_Event]:
    try:
      return self._storage._list()
    except  Exception as ex:
      raise   DB_Exception(f"Error listing events: {ex}")
  def _update(self,_id:str,_topic:str,_content:str):
    try:
      return  self._storage._update(_id,_topic,_content)
    except   Exception as ex:
      raise   DB_Exception(f"Error updating event: {ex}")
  def  _delete(self,_id:str):
    try:
      return   self._storage._delete(_id)
    except   Exception as ex:
      raise DB_Exception(f"Error deleting event: {ex}")
    



  







  