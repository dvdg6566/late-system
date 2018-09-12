import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pymongo import MongoClient
import datetime
import json

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
    students.drop()
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
    fn = "Archive " + str(now.day) + "-"  + str(now.month) + "-" + str(now.year) + " at " + str(now.hour) + ":"
    if now.minute<10: fn += "0"
    fn += str(now.minute) + ".csv"
    cols = "StudentId,date,time,name,class\n"
    output = open("./csvFiles/" + fn + ".csv","w")
    output.write(cols)
    for log in occ.find():
        i = [str(log[x]) for x in log.keys() if x != '_id']
        output.write(','.join(i) + '\n')
    output.close()
    occ.drop()
    return json.dumps(fn)

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
        return []

def send_email(id):
    global students,occ
    now = datetime.datetime.now()
    N = 0
    for i in occ.find({"StudentId": id}): N += 1
    f = students.find_one({"card_number": id})
    text = "Dear " + f["form_teacher_one"] + " and " + f["form_teacher_two"] + ",\n\nThis is an email to inform you that " + f["name"] + " from class " + f["class"] + " has left school early on " + now.strftime("%d-%m-%Y") + " at " + now.strftime("%H:%M") + ".\n\n"
    if(N != 1):text += "He has left school early " + str(N) + " times."
    else:text += "He has only left school early once."
    text += "\n\nThank you."
    email(f['teachers_emails'],text,f["name"])

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("cepy3testing@gmail.com", "testing777")

def smpt_connect():
    global server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("cepy3testing@gmail.com", "testing777")

def email(toaddr,text,name):
    global server
    fromaddr = "cepy3testing@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Student " + name + " leaving early from school"
    msg.attach(MIMEText(text, 'plain'))
    try:
        server.sendmail(fromaddr,toaddr, msg.as_string())
    except:
        smpt_connect()
        server.sendmail(fromaddr,fromaddr, msg.as_string())