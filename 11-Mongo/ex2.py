import datetime
from pprint import pprint

from bson import Decimal128, ObjectId, SON
from pymongo import MongoClient

client = MongoClient()

db = client.get_database("my_test_db")
coll = db.get_collection("example")

doc = {
    'name': 'John Doe',
    'age': 40,
    'pi': 3.14,
    'created_at': datetime.datetime(2010, 12, 31, 9, 55),
    'nothing_here': None,
    'is_happy': True,
    'ratio': Decimal128("1.2500"),

    'colors': ['red', 'green', 'blue'],

    'ice_cream': {
        'waffle': True,
        'flavours': ['vanilla', 'strawberry'],
        'price': 12.95,
    },
    'some_other_doc_id': ObjectId("0123456789ab0123456789ab"),
}

result = coll.insert_one(doc)
print(result.inserted_id)

o = coll.find_one({'_id': result.inserted_id})
pprint(o)