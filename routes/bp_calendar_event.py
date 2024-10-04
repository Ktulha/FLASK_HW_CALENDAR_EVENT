
from flask import Blueprint, request

from model.calendar_event import CalendarEvent

from api.Calendar_Event.logic import CalendarEventLogic

class CalendarEventError(Exception):
    """Base class for all exceptions in this module"""
    pass

_logic=CalendarEventLogic()

def _from_raw(raw_data) -> CalendarEvent:
    parts=raw_data.split('|')
    if len(parts) != 3:
        raise CalendarEventError(f'Invalid data {raw_data}')
    _event=CalendarEvent()
    _event.date=parts[0]
    _event.topic=parts[1]
    _event.content=parts[2]
    return  _event

def _to_raw(_event: CalendarEvent) -> str:
    return f'{_event._id}|{_event.date}|{_event.topic}|{_event.content}'

    
        


calendar_event_route=Blueprint('calendar_event_route',__name__,url_prefix='/api/v1/calendar')

@calendar_event_route.route('/',methods=['GET','POST'])
def list_and_create():
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
    if request.method=='GET':
        try:
            return  _logic._read(_id)
        except Exception  as e:
            return  f"Error: {e}",404
    elif request.method=='PUT':
        try:
            _logic._update(_id,_from_raw(request.get_data().decode('utf-8')))
            return   f'Updated { _id }',200

        except  Exception  as e:
            return  f"Error: {e}",404
    elif request.method=='DELETE':
        try:
             _logic._delete(_id)
             return f'Event id:  {_id} deleted',200

        except  Exception  as e:
            return  f"Error: {e}",404
        

        



