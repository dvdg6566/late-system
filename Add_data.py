import pymongo,pprint
def add_sample_data():
    client = pymongo.MongoClient()
    students = client.cepfp.studentdata
    logs = client.cepfp.studentlogs

    new_students = [
        {"name": "Jotham Lim", "card_number": "T0312345A", "class": "2S", "form_teacher_one": "Ms Yong Tau Foo",
            "form_teacher_two": "Mr Sir Dab Boi", "teachers_emails": ["czhdaniel@gmail.com", "jothamlimjlj@gmail.com"]},
        {"name": "sirboi tan", "card_number": "T0423123H", "class": "3F", "form_teacher_one": "Ms Yong Tau Foo",
            "form_teacher_two": "Mr Sir Dab Boi", "teachers_emails": ["czhdaniel@gmail.com", "jothamlimjlj@gmail.com"]},
        {"name": "Binner Neo", "card_number": "T0098765A", "class": "3D", "form_teacher_one": "Ms Yong Tau Foo",
            "form_teacher_two": "Mr Sir Dab Boi", "teachers_emails": ["czhdaniel@gmail.com", "jothamlimjlj@gmail.com"]},
        {"name": "Dabniel Boon", "card_number": "T0218390D", "class": "3E", "form_teacher_one": "Ms Yong Tau Foo",
            "form_teacher_two": "Mr Sir Dab Boi", "teachers_emails": ["czhdaniel@gmail.com", "jothamlimjlj@gmail.com"]},
        {"name": "Yin Jun", "card_number": "T0369696B", "class": "1A", "form_teacher_one": "Ms Yong Tau Foo",
            "form_teacher_two": "Mr Sir Dab Boi", "teachers_emails": ["czhdaniel@gmail.com", "jothamlimjlj@gmail.com"]},
        {"name": "LYH", "card_number": "T0371111L", "class": "2I", "form_teacher_one": "Ms Yong Tau Foo",
            "form_teacher_two": "Mr Sir Dab Boi", "teachers_emails": ["czhdaniel@gmail.com", "jothamlimjlj@gmail.com"]}
    ]
    students.drop()  # Clear the students collection in the test database
    students.insert_many(new_students)

    #pprint(students.find_one({"card_number": "T0312345A"}))
    a = []
    for i in new_students:
        N = i["card_number"]
        a.append({"StudentId": N, "Occurence": 0})
    logs.drop()
    logs.insert_many(a)
    for i in logs.find():
        pprint(i)
