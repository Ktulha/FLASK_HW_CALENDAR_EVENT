from model.calendar_event import Calendar_Event

class StorageExceptions(Exception):
  pass

class Calendar_Events_Storage:
  def __init__(self):
    self._id_iterator=0
    self._storage= {}
    self._dates=[]
    
  def _create(self,_event:Calendar_Event)->str:
    if _event._date in self._dates:
      raise  StorageExceptions("Event date is  already in storage")
    self._id_iterator+=1
    _event._id=str(self._id_iterator)
    self._storage[_event._id]=_event
    return _event._id
    
  def _read(self,_id:str)->Calendar_Event:
    if _id not in self._storage:
      raise  StorageExceptions(f"Event {_id} not found")
    return  self._storage[_id]


  def _list(self)->list[Calendar_Event]:
    return list(self._storage.values())
  
  def _update(self,_id:str,_topic:str,_context:str):
    if _id not in  self._storage:
      raise StorageExceptions(f"Event {_id} not found")
    self._storage[_id]._topic=_topic
    self._storage[_id]._context=_context
    
  def  _delete(self,_id:str):
    if  _id not in self._storage:
      raise StorageExceptions(f"Event {_id} not found")
    del  self._storage[_id]


