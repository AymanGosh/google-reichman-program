from pymongo import MongoClient

client = MongoClient()
# client = MongoClient(host="127.0.0.1")

db = client.get_database("my_test_db")
users = db.get_collection("users")
print(type(users))  # <class 'pymongo.collection.Collection'>

user_info = {
    'name': 'John Lennon',
    'email': 'john@beatles.com',
    'phone': '5555-555',
}

result = users.insert_one(user_info)

print(type(result))  # <class 'pymongo.results.InsertOneResult'>
uid = result.inserted_id
print(type(uid))  # <class 'bson.objectid.ObjectId'>
print(uid)  # 5c63fd645409a94b452ccab9