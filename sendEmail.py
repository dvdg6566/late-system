import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pymongo
from pprint import pprint
import datetime
import json

def send_email(id):
    client = pymongo.MongoClient()
    students = client.cepfp.studentdata
    logs = client.cepfp.studentlogs
    now = datetime.datetime.now()
    N = logs.find_one({"StudentId": id})["Occurence"]
    #print(json.dumps(id))
    f = students.find_one({"card_number": id})
    text = "Dear " + f["form_teacher_one"] + " and " + f["form_teacher_two"] + ",\n\nThis is an email to inform you that " + f["name"] + " from class " + f["class"] + " has left school early on " + now.strftime("%d-%m-%Y") + " at " + now.strftime("%H:%M") + ".\n\nHe has left school early " + str(N) + " times.\n\nThank you."
    email(f['teachers_emails'],text,f["name"])


def email(toaddr,text,name):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("cepy3testing@gmail.com", "testing777")

    fromaddr = "cepy3testing@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = ", ".join(toaddr)
    msg['Subject'] = "Student " + name + " leaving early from school"
    msg.attach(MIMEText(text, 'plain'))

    server.sendmail(fromaddr,toaddr, msg.as_string())
    server.quit()

#email("czhdaniel@gmail.com","TEST")
#send_email("T0312345A")
