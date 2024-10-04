from flask import Flask, request

app = Flask(__name__)

@app.route("/",methods=['GET','POST','PUT','DELETE'])
def hello():
    return 'request.content_type'