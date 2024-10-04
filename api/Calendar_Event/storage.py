from model.calendar_event import CalendarEvent


    
class StorageException(Exception):
    """Base class for all storage-related exceptions."""
    pass

class CalendarEventStorage:
    def __init__(self) -> None:
       self._id_iterator=0
       self._events={}
       self._dates={}
    
    def _create(self,_event:CalendarEvent) -> str:
        """Create a new event and return its id"""
        if _event.date in self._dates:
            raise  StorageException(f"Event date {_event.date} already exists")

        self._id_iterator += 1
        _event._id=str(self._id_iterator)
        self._events[_event._id]=_event
        self._dates[_event.date]=_event._id
        return  _event._id

    def _read(self,_id:str)->CalendarEvent:
        """Read an event by its id"""
        if _id not in self._events:
            raise StorageException("Event not found")
        return self._events[_id]

    def _list(self)->list[CalendarEvent]:
           """Return a list of all events"""
           return  list(self._events.values())

    def _update(self,_id:str,_event:CalendarEvent):
        """Update an event by its id"""
        if self._dates.get(_event.date,_id)!=_id :
            raise StorageException(f"Event date {_event.date} already exists")
        elif _id not in self._events:
            raise StorageException(f"Event {_id} not found")
        else:
            del self._dates[self._events[_id].date]
            _event._id=_id
            self._events[_id]=_event
            self._dates[_event.date]=_event._id
        


    def _delete(self,_id:str):
        """Delete an event by its id"""
        if _id not in self._events:
            raise  StorageException("Event not found")
        del self._dates[self._events[_id].date]
        del self._events[_id]

        
           


        

        