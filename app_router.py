from flask import Flask, request

from routes.bp_calendar_event import calendar_event_route


app = Flask(__name__)

app.register_blueprint(calendar_event_route)