import pprint
import pymongo

def main():
    # 1. Connect to MongoDB instance running on localhost
    client = pymongo.MongoClient()
    #client.test.restaurants.drop() # Clear the restaurants collection in the test database
    # Access the 'restaurants' collection in the 'test' database
    collection = client.test.restaurants

    # 2. Insert
    new_documents = [
        {"name": "Sun Bakery Trattoria", "stars": 0, "categories": [
            "Pizza", "Pasta", "Italian", "Coffee", "Sandwiches"]},
        {"name": "Blue Bagels Grill", "stars": 1,
            "categories": ["Bagels", "Cookies", "Sandwiches"]},
        {"name": "Hot Bakery Cafe", "stars": 2, "categories": [
            "Bakery", "Cafe", "Coffee", "Dessert"]},
        {"name": "XYZ Coffee Bar", "stars": 3, "categories": [
            "Coffee", "Cafe", "Bakery", "Chocolates"]},
        {"name": "456 Cookies Shop", "stars": 4, "categories": [
            "Bakery", "Cookies", "Cake", "Coffee"]}
    ]

    #collection.insert_many(new_documents)

    # 3. Update

    collection.update(
        {"name": "Sun Bakery Trattoria"},
        {
            "name": "Sun Bakery Trattoria",
            "stars": 2,
            "categories": ["Pizza", "Pasta", "Italian", "Coffee", "Sandwiches"]
        }
    )

    # 3b.Update including whatever is there. Takes in name, attribute, and increment.
    def update_one(name, att, inc):
        s = collection.find_one({"name": "Sun Bakery Trattoria"})
        s[att] += inc
        collection.update({"name": name}, s)

    update_one("Sun Bakery Trattoria", "stars", 3)

    # 4. Query
    for restaurant in collection.find():
        pprint.pprint(restaurant)


if __name__ == '__main__':
    main()
