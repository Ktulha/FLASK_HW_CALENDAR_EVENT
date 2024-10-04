
from flask import Blueprint, request

from model.calendar_event import CalendarEvent

from api.Calendar_Event.logic import CalendarEventLogic

class CalendarEventError(Exception):
    """Base class for all exceptions in this module"""
    pass

_logic=CalendarEventLogic()

def _from_raw(raw_data) -> CalendarEvent:
    parts=raw_data.split('|')
    if len(raw_data) != 3:
        raise CalendarEventError('Invalid data')
    _event=CalendarEvent()
    _event.date=parts[0]
    _event.topic=parts[1]
    _event.content=parts[2]
    return  _event

def _to_raw(_event: CalendarEvent) -> str:
    return f'{_event.id}{_event.date}|{_event.topic}|{_event.content}'

    
        


calendar_event_route=Blueprint('calendar_event_route',__name__,url_prefix='/api/v1/calendar')

@calendar_event_route.route('/',methods=['GET','POST'])
def list_and_create() :
    if request.method=='GET':
        try:
            return _logic._list()
        except Exception  as e:
            raise  CalendarEventError(str(e)) from e
    elif  request.method=='POST':
        try:
            return _logic._create(_from_raw(request.get_data()))
        except Exception  as e:
            raise  CalendarEventError(str(e)) from e




@calendar_event_route.route('/<_id>',methods=['GET','PUT','DELETE'])
def read_update_delete(_id):
    if request.method=='GET':
        try:
            return  _logic._read(_id)
        except Exception  as e:
            raise  CalendarEventError(str(e)) from e
    elif request.method=='PUT':
        try:
            return _logic._update(_id,_from_raw(request.get_data()))
        except  Exception  as e:
            raise   CalendarEventError(str(e)) from e
    elif request.method=='DELETE':
        try:
            return _logic._delete(_id)
        except  Exception  as e:
            raise  CalendarEventError(str(e)) from e
        

        



