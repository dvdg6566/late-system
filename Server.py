from flask import Flask, render_template, request, jsonify
from sendEmail import send_email
import json

app = Flask(__name__)

@app.route('/')
def route():
    return "Connected!"

@app.route('/email',methods=["POST"])
def send():
   #print(json.dumps(request.data))
    N = json.loads(request.data)        #Get user data from manual input
    send_email(N)
    return json.dumps("HELLO")

if __name__ == '__main__':
   app.run(debug=True, threaded=True, host="0.0.0.0")
