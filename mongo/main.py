from pymongo import MongoClient
from bson.objectid import ObjectId

uri = "localhost:27017"
client = MongoClient(uri)
try:
    database = client.get_database("data")
    # database.create_collection('new')
    users = database.get_collection("users")
    # Query for a movie that has the title 'Back to the Future'
    query = { "_id": {"$in": [ObjectId('66e46a030c9eb4602ee82c52'), ObjectId('65a17350ceb1ebf5e524438b')]} }
    user = list(users.find(query))
    print(users.count_documents({}))
    print(user)
    client.close()
except Exception as e:
    raise Exception("Unable to find the document due to the following error: ", e)