from pprint import pprint

from pymongo import MongoClient

client = MongoClient()

db = client.get_database("my_test_db")
users = db.get_collection("users")

users_info = [
    {
        'name': 'Mickey Mouse',
        'email': 'mickey@disney.com',
    },
    {
        'name': 'Donald Duck',
        'email': 'donald@disney.com',
    },
    {
        'name': 'Goofy',
        'email': 'goofy@disney.com',
    },
]
users.insert_many(users_info)

print(users.count_documents({})) # actual count
print(users.estimated_document_count())  # from metadata

cur = users.find()
print(type(cur))
for d in cur:  # <class 'pymongo.cursor.Cursor'>
    pprint(d)