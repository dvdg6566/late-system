import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pymongo
from pprint import pprint
import datetime
import json
import pandas as pd
import numpy as np
from math import floor

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("cepy3testing@gmail.com", "testing777")
client = pymongo.MongoClient()
logs = client.cepfp.studentlogs
students = client.cepfp.studentdata
occ = client.cepfp.occurencelogs

def upload(df):
    global logs, students, occ
    students.drop()
    new_students = [{} for i in range(df.shape[0])]
    col = df.columns
    for i in range(df.shape[0]):
        for j in col:
            new_students[i][j] = df[j][i]
    students.insert_many(new_students)
    a = []
    for i in new_students:
        N = i["card_number"]
        a.append({"StudentId": N, "Occurence": 0})
    logs.drop()
    logs.insert_many(a)
    length,ctr = 0,-1
    x = occ.find()
    for i in x:
        length += 1
    cols = ["StudentId", "date", "time", "name", "class"]
    df = pd.DataFrame(np.ones(5*length).reshape(-1,5),columns=cols)
    for i in occ.find():
        ctr += 1
        for j in cols:
            df[j][ctr] = i[j]
    now = datetime.datetime.now()
    fn = "Archive " + str(now.day) + "-"  + str(now.month) + "-" + str(now.year) + " at " + str(now.hour) + ":"
    if now.minute<10: fn += "0"
    fn += str(now.minute) + ".csv"

    occ.drop()
    df.to_csv("csvFiles/" + fn)
    return json.dumps(fn)

def new_student(id):
    global logs, students
    try:
        s = logs.find_one({"StudentId": id})
        s["Occurence"] += 1
        logs.update({"StudentId": id}, s)
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
    global students, logs
    try:
        D = {}
        s = logs.find_one({"StudentId": id})
        D["Occurence"] = s["Occurence"]
        s = students.find_one({"card_number": id})
        D["name"] = s["name"]
        D["class"] = s["class"]
        return D
    except TypeError:
        return []

def send_email(id):
    global client,students,logs
    now = datetime.datetime.now()
    N = logs.find_one({"StudentId": id})["Occurence"]
    #print(json.dumps(id))
    f = students.find_one({"card_number": id})
    text = "Dear " + f["form_teacher_one"] + " and " + f["form_teacher_two"] + ",\n\nThis is an email to inform you that " + f["name"] + " from class " + f["class"] + " has left school early on " + now.strftime("%d-%m-%Y") + " at " + now.strftime("%H:%M") + ".\n\n"
    if(N != 1):
        text += "He has left school early " + str(N) + " times."
    else:
        text += "He has only left school early once."
    text += "\n\nThank you."
    email(f['teachers_emails'],text,f["name"])

def email(toaddr,text,name):
    global server
    b = [i.split('"')[1] for i in toaddr.split('[')[1].split(']')[0].split(",")]
    fromaddr = "cepy3testing@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = ", ".join(b)
    msg['Subject'] = "Student " + name + " leaving early from school"
    msg.attach(MIMEText(text, 'plain'))

    server.sendmail(fromaddr,b, msg.as_string())
