from pprint import pprint
import pymongo

client = pymongo.MongoClient()
logs = client.cepfp.studentlogs
students = client.cepfp.studentdata

def new_student(id):
    global logs
    try:
        s = logs.find_one({"StudentId":id})
        s["Occurence"] += 1
        logs.update({"StudentId":id},s)
        return 0
    except TypeError:
        return -1


def query_student(id):
    global students,logs
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

