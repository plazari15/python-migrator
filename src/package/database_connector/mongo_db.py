import pymongo
from ..config import mongodb

def connect():
    mongo_client = pymongo.MongoClient(mongodb.MONGODB_URI)
    return mongo_client[mongodb.MONGODB_DATABASE]
