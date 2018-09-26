from flask import Flask, render_template, request, jsonify
import json
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pymongo import MongoClient
import datetime
from flask_cors import CORS

client = MongoClient()
occ = client.cep.occ # Gets Collection occurences from database CEP
students = client.cep.students #Gets collections students from database CEP

def Dayquery(s):
    global occ
    x = occ.find({"date": int(s)})
    if (len(str(s)) != 8):
        return json.dumps("Invalid Date")
    l = 0
    for i in x:
        l+=1
    arr = [{} for i in range(l)]
    if l == 0:
        return json.dumps("No Students were late on this date")
    x = occ.find({"date": int(s)})
    for i in range(l):
        arr[i]["name"] = x[i]["name"]
        arr[i]["class"] = x[i]["class"]
        arr[i]["time"] = x[i]["time"]
    return json.dumps(arr)

def download(df):
    global students, occ
    students.drop() #Replaces the student database by clearing existing students
    new_students = [{} for i in range(df.shape[0])]
    col = df.columns
    for i in range(df.shape[0]):
        for j in col:
            new_students[i][j] = df[j][i]
    students.insert_many(new_students)
    return export()

def export():
    global occ
    now = datetime.datetime.now()
    fn = "Logs " + str(now.day) + "-"  + str(now.month) + "-" + str(now.year) + " at " + str(now.hour) + ":"
    if now.minute<10: fn += "0"
    fn += str(now.minute) + ".csv"
    cols = "StudentId,name,date,time,class\n"
    output = open(fn,"w") #Writes the headers into the csv
    output.write(cols)
    for log in occ.find():
        i = [None for i in range(5)] #we populate this array with the entries into the csv file then we appending to the bottom of the csv files
        i[0] = log["StudentId"]
        i[1] = log["name"]
        i[2] = str(log["date"])
        i[3] = str(log["time"])
        i[4] = log["class"]
        output.write(','.join(i) + '\n') #We convert the array into a comma-separated string
    output.close()
    occ.drop() #Clears the database
    return json.dumps("Desktop/" + fn)

def new_student(id):
    global students
    try:
        P = students.find_one({"card_number": id})
        now = datetime.datetime.now()
        date = now.year*10000+now.month*100+now.day
        time = now.hour*10000+now.minute*100+now.second
        obj = {
            "StudentId":id,
            "date":date,
            "time":time,
            "name": P["name"],
            "class": P["class"]
        }
        occ.insert_one(obj)
        return P["name"]
    except TypeError:
        return -1

def query_student(id):
    global students, occ
    try:
        D = [{},[]]
        s = students.find_one({"card_number": id})
        D[0]["name"] = s["name"]
        D[0]["class"] = s["class"]
        s = occ.find({"StudentId":id})
        for i in s:
            D[1].append({})
            D[1][-1]["date"] = i["date"]
            D[1][-1]["time"] = i["time"]
        return D
    except TypeError:
        return [] #The type error triggers if the student does not exist.

def send_email(id):
    global students,occ
    now = datetime.datetime.now()
    N = 0
    for i in occ.find({"StudentId": id}): N += 1 # Get the number of times the student has left early
    f = students.find_one({"card_number": id})
    text = "Dear " + f["form_teacher_one"] + " and " + f["form_teacher_two"] + ",\n\nThis is an email to inform you that " + f["name"] + " from class " + f["class"] + " has left school early on " + now.strftime("%d-%m-%Y") + " at " + now.strftime("%H:%M") + ".\n\n"
    if(N != 1):text += "He has left school early " + str(N) + " times."
    else:text += "He has only left school early once."
    text += "\n\nThank you."
    email(f['teachers_emails'],text,f["name"])

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("cepy3testing@gmail.com", "testing777")

def smtp_connect():
    global server
    server = smtplib.SMTP('smtp.gmail.com', 587) # To be replaced by legitimate details
    server.starttls()
    server.login("cepy3testing@gmail.com", "testing777") #To be replaced by legitimate details

def email(toaddr,text,name):
    global server
    fromaddr = "cepy3testing@gmail.com" #To be changed for legitimate email
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Student " + name + " leaving early from school"
    msg.attach(MIMEText(text, 'plain'))
    try:
        server.sendmail(fromaddr,toaddr, msg.as_string())
    except:
        smtp_connect() #If fails, that means server has timed out. Restart the server.
        server.sendmail(fromaddr,fromaddr, msg.as_string())

app = Flask(__name__)
CORS(app) #Enables the web UI to have permission to access the localhost:5000

@app.route('/email',methods=["POST"])
def send():
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

@app.route('/downloadLogs', methods=["POST"])
def run():
    return download(pd.read_csv(request.files['studentdb']))

@app.route('/downloadLogsWithoutReplacement', methods=["POST"])
def IneedAname():
    return export()

@app.route('/queryDay',methods=["POST"])
def process():
    N = json.loads(request.data)
    return Dayquery(N)

if __name__ == '__main__':
   app.run(debug=True, threaded=True, host="0.0.0.0")
