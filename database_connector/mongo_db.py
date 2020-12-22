from dotenv import load_dotenv, find_dotenv
import pymongo
import os


load_dotenv(find_dotenv())

def connect():
    mongo_client = pymongo.MongoClient(os.environ.get('MONGODB_URI'))
    return mongo_client[os.environ.get('MONGO_DB')]
