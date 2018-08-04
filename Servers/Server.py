from flask import Flask, render_template, request, jsonify
from db import *
import json
import pandas as pd

app = Flask(__name__)

@app.route('/')
def route():
    return "Connected!"

@app.route('/email',methods=["POST"])
def send():
   #print(json.dumps(request.data))
    N = json.loads(request.data)        #Get user data from manual input
    name = new_student(N)
    if name == -1:
        return json.dumps("Error")
    send_email(N)
    return json.dumps(name)

@app.route('/query', methods=["POST"])
def query():
   #print(json.dumps(request.data))
    N = json.loads(request.data)  # Get user data from manual input
    return json.dumps(query_student(N))

@app.route('/uploads', methods=["POST"])
def run():
    return upload(pd.read_csv(request.files['studentdb']))

if __name__ == '__main__':
   app.run(debug=True, threaded=True, host="0.0.0.0")