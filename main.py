from flask import Flask, request

from routes import bp_calendar_event

app = Flask(__name__)

app.register_blueprint(bp_calendar_event)

if __name__ == "__main__":
    app.run()