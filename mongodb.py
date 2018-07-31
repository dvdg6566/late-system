import pprint
import pymongo
"""
def main():
    client = pymongo.MongoClient()  # 1. Connect to MongoDB instance running on localhost
    #client.test.restaurants.drop() # Clear the restaurants collection in the test database
    collection = client.test.restaurants # Access the 'restaurants' collection in the 'test' database

    # 2. Insert 
    new_documents = [
        {"name":"Sun Bakery Trattoria", "stars":0, "categories":["Pizza","Pasta","Italian","Coffee","Sandwiches"]},
        {"name":"Blue Bagels Grill", "stars":1, "categories":["Bagels","Cookies","Sandwiches"]},
        {"name":"Hot Bakery Cafe","stars":2,"categories":["Bakery","Cafe","Coffee","Dessert"]},
        {"name":"XYZ Coffee Bar","stars":3,"categories":["Coffee","Cafe","Bakery","Chocolates"]},
        {"name":"456 Cookies Shop","stars":4,"categories":["Bakery","Cookies","Cake","Coffee"]}
    ]

    #collection.insert_many(new_documents)

    # 3. Update
    
    collection.update(
        {"name":"Sun Bakery Trattoria"},
        {
            "name": "Sun Bakery Trattoria", 
            "stars": 2, 
            "categories": ["Pizza", "Pasta", "Italian", "Coffee", "Sandwiches"]
        }
    )
    
    # 3b.Update including whatever is there. Takes in name, attribute, and increment. 
    def update_one(name,att,inc):
        s = collection.find_one({"name": "Sun Bakery Trattoria"})
        s[att]+=inc
        collection.update({"name":name},s)

    update_one("Sun Bakery Trattoria","stars",3)


    # 4. Query
    for restaurant in collection.find():
        pprint.pprint(restaurant)


if __name__ == '__main__':
    main()
"""


client  = pymongo.MongoClient()
students = client.cepfp.studentdata

new_students = [
    {"name":"Jotham Lim","card_number":"T0312345A", "class": "2S", "form_teacher_one":"Ms Yong Tau Foo", "form_teacher_two": "Mr Sir Dab Boi", "teachers_emails":["czhdaniel@gmail.com","jothamlimjlj@gmail.com"]},
    {"name": "sirboi tan", "card_number": "T0423123H", "class": "3F", "form_teacher_one": "Ms Yong Tau Foo","form_teacher_two": "Mr Sir Dab Boi", "teachers_emails": ["czhdaniel@gmail.com","jothamlimjlj@gmail.com"]},
    {"name": "Binner Neo", "card_number": "T0098765A", "class": "3D", "form_teacher_one": "Ms Yong Tau Foo", "form_teacher_two": "Mr Sir Dab Boi", "teachers_emails": ["czhdaniel@gmail.com","jothamlimjlj@gmail.com"]},
    {"name": "Dabniel Boon", "card_number": "T0218390D", "class": "3E", "form_teacher_one": "Ms Yong Tau Foo", "form_teacher_two": "Mr Sir Dab Boi", "teachers_emails": ["czhdaniel@gmail.com","jothamlimjlj@gmail.com"]},
    {"name": "Yin Jun", "card_number": "T0369696B", "class": "1A", "form_teacher_one": "Ms Yong Tau Foo", "form_teacher_two": "Mr Sir Dab Boi", "teachers_emails": ["czhdaniel@gmail.com","jothamlimjlj@gmail.com"]}]
#students.drop() # Clear the students collection in the test database
#students.insert_many(new_students)

pprint.pprint(students.find_one({"card_number": "T0312345A"}))
"""

"""
