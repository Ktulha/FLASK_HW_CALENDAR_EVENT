from flask import Blueprint,request

from api.calendar_event._logic import Calendar_Events_Logic
from model.calendar_event import Calendar_Event

class APIException(Exception):
  pass

event_logic=Calendar_Events_Logic()

def _from_raw(raw_data:str)-> Calendar_Event:
  parts=raw_data.split('|')
  if len(parts)==3:
    _event=Calendar_Event()
    _event._id=None
    try:
      _event._id=int(parts[0])
    except  ValueError:
      _event._date=parts[0]
    else:
      raise APIException("Unknown error")
    
    _event._topic=parts[1]
    _event._content=parts[2]
  else:
    raise APIException(f"invalid RAW data: {raw_data}")
  return _event

def _to_raw(_event:Calendar_Event)->str:
  return f"{_event._id}|{_event._date}|{_event._topic}|{_event._content}"



calendar_event_route=Blueprint('calendar_event_route', __name__, url_prefix='/api/v1/calendar/')

@calendar_event_route.route('/',methods=['GET'])
def events_to_list():
  try:
    _events=event_logic._list()
    for e  in _events:
      raw_data=""
      raw_data+=_to_raw(e)+'\n'
    return raw_data,200
  except Exception as ex:
    raise  APIException(f"Error: {str(ex)}")

@calendar_event_route.route('/',methods=['POST'])
def  create():
  try:
    raw_data=request.get_data().decode('utf-8')
    _event=_from_raw(raw_data)
    _id=event_logic._create(_event)
    return  f"Event created. New id: {_id}",201
  except Exception as ex:
    return  f"Error: {str(ex)}",404
  
@calendar_event_route.route('/<_id>',methods=['GET','PUT','DELETE'])
def read_update_delete(_id:str):
  match  request.method:
    case  'GET':
      try:
        _event=event_logic._read(_id)
        return _to_raw(_event),200
      except Exception as ex:
        return f"Error: {str(ex)}",404
    case   'PUT':
      try:
        _event=_from_raw(request.get_data().decode('utf-8'))
        event_logic._update(_id,_event)
        return f"Event id: {_id} updated. ",200
      except  Exception as ex:
        return f"Error: {str(ex)}",404
    case 'DELETE':
      try:
        event_logic._delete(_id)
        return f"Event id: {_id} deleted. ",200
      except  Exception as ex:
        return f"Error: {str(ex)}",404
    




   
    
  

