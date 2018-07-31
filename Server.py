from flask import Flask, render_template, request, jsonify
from sendEmail import send_email
from logDB import new_student,query_student
import json

app = Flask(__name__)

@app.route('/')
def route():
    return "Connected!"

@app.route('/email',methods=["POST"])
def send():
   #print(json.dumps(request.data))
    N = json.loads(request.data)        #Get user data from manual input
    new_student(N)
    send_email(N)
    return json.dumps("HELLO")


@app.route('/query', methods=["POST"])
def query():
   #print(json.dumps(request.data))
    N = json.loads(request.data)  # Get user data from manual input
    return json.dumps(query_student(N))

if __name__ == '__main__':
   app.run(debug=True, threaded=True, host="0.0.0.0")
