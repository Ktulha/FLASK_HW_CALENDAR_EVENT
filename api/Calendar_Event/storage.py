from model.calendar_event import CalendarEvent

class StorageException(Exception):
    """Base class for all storage-related exceptions."""
    pass

class CalendarEventStorage:
    def __init__(self):
        _id_iterator=0
        _events={}
        _dates=[]
    
    def _create(self,_event:CalendarEvent)->str:
        """Create a new event and return its id"""
        if _event.date in _dates:
            raise  StorageException(f"Event date {_event.date} already exists")
                    
        _id_iterator+=1
        _event._id=str(_id_iterator)
        _events[_event._id]=_event
        _dates.append(_event.date)
        return  _event._id
    
    def _read(self,_id:str)->CalendarEvent:
        """Read an event by its id"""
        if _id not in _events:
            raise StorageException("Event not found")
        return _events[_id]
    
    def _list(self)->list[CalendarEvent]:
        """Return a list of all events"""
        return  list(_events.values())
    
    def _update(self,_id:str,_event:CalendarEvent):
        """Update an event by its id"""
        if _id not in _events:
            raise StorageException(f"Event {_id} not found")
        if _event.date not in  _dates:
            raise StorageException(f"Event date {_event.date} already exists")
        _event._id=_id
        _events[_id]=_event
        
    
    def _delete(self,_id:str):
        """Delete an event by its id"""
        if _id not in _events:
            raise  StorageException("Event not found")
        del _events[_id]
        _dates.remove(_events[_id].date)


        

        