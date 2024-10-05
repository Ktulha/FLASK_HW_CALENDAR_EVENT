
from flask import Blueprint, request

from model.calendar_event import CalendarEvent

from api.Calendar_Event.logic import CalendarEventLogic

class CalendarEventError(Exception):
    """Base class for all exceptions in this module"""
    pass

_logic=CalendarEventLogic()

def _from_raw(raw_data) -> CalendarEvent:
    """Convert a raw string of event data into a CalendarEvent object.

    This function expects the input string to be formatted with three parts separated by a pipe ('|') character. 
    If the format is incorrect, it raises a CalendarEventError.

    Args:
        raw_data (str): The raw string containing event data.

    Returns:
        CalendarEvent: The constructed CalendarEvent object.

    Raises:
        CalendarEventError: If the input string does not contain exactly three parts.
    """
    parts=raw_data.split('|')
    if len(parts) != 3:
        raise CalendarEventError(f'Invalid data {raw_data}')
    _event=CalendarEvent()
    _event.date=parts[0]
    _event.topic=parts[1]
    _event.content=parts[2]
    return  _event

def _to_raw(_event: CalendarEvent) -> str:
    """Convert a CalendarEvent object into a raw string of event data."""
    return f'{_event._id}|{_event.date}|{_event.topic}|{_event.content}'

    
        


calendar_event_route=Blueprint('calendar_event_route',__name__,url_prefix='/api/v1/calendar')

@calendar_event_route.route('/',methods=['GET','POST'])

def list_and_create():
    """Handle HTTP requests for listing and creating calendar events.

    This function processes GET requests to retrieve a list of calendar events and POST requests to create a new event. 
    It interacts with the logic layer to perform the corresponding operations and returns appropriate responses.

    Returns:
        str: A string representation of the list of events for GET requests or a message indicating the creation of a new event for POST requests.

    Raises:
        Exception: If an error occurs during the listing or creation of events.
    """
    if request.method=='GET':
        try:
            return "\n".join(_to_raw(_event) for _event in _logic._list())
            
        except Exception  as e:
            return  f"Error: {e}"
    elif  request.method=='POST':
        try:
            _id= _logic._create(_from_raw(request.get_data().decode('utf-8') ))
            return  f'Created { _id }',200

        except Exception  as e:
            return  f"Error: {e}",404




@calendar_event_route.route('/<_id>',methods=['GET','PUT','DELETE'])
def read_update_delete(_id:str):
    """Handle HTTP requests for reading, updating, and deleting calendar events.

    This function processes GET, PUT, and DELETE requests for a specific calendar event identified by its id. 
    It interacts with the logic layer to perform the corresponding operations and returns appropriate responses.

    Args:
        _id (str): The unique identifier of the calendar event.

    Returns:
        str: A message indicating the result of the operation, along with the HTTP status code.

    Raises:
        Exception: If an error occurs during the read, update, or delete operations.
    """
    
    if request.method=='GET':
        try:
            return  _logic._read(_id)
        except Exception  as e:
            return  f"Error: {e}",404
    elif request.method=='PUT':
        try:
            _logic._update(_id,_from_raw(request.get_data().decode('utf-8')))
            return   f'Updated { _id }',201

        except  Exception  as e:
            return  f"Error: {e}",404
    elif request.method=='DELETE':
        try:
             _logic._delete(_id)
             return f'Event id:  {_id} deleted',200

        except  Exception  as e:
            return  f"Error: {e}",404
        

        



