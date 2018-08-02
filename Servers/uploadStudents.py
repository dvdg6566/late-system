from pprint import pprint
import pymongo
import pandas as pd

client = pymongo.MongoClient()
logs = client.cepfp.studentlogs
students = client.cepfp.studentdata

def upload(df):
    global logs,students
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
        r = logs.find_one({"StudentId" : N})
        if r != None:
            a.append({"StudentId": N, "Occurence": r["Occurence"]})
        else:
            a.append({"StudentId": N, "Occurence": 0})
    logs.drop()
    logs.insert_many(a)
    for i in logs.find():
        pprint(i)
