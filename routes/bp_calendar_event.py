'''
В идеале нужно забрать какие-то данные в единый интерфейс. передать их в логику и там разбираться что это такое, определять content-type, method  и тд.

'''
from flask import Blueprint,request,jsonify,render_template,url_for

from api.calendar_event import _logic


bp_calendar_event=Blueprint('bp_calendar_event',__name__,url_prefix='/api/v1/calendar_event/')

@bp_calendar_event.route('/',methods=['GET','POST'])
def index():
  if request.method == 'GET':
    _logic
  elif request.method=='POST':
    pass
  else:
    return jsonify({'error':'method not allowed'}),405

