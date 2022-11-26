from flask import Flask
from flask import Response
import sys

app = Flask(__name__)

@app.route("/")
def hello():
    resp = Response('{ "André" : "Service running. Python version: ' + sys.version + '"}')
    resp1 = Response('{ "message" }')
    resp.headers['Content-Type'] = 'application/json'
    resp1.headers['Content-Type'] = 'application/json'
    return resp, resp1
