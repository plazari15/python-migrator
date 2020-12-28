from src.database_connector import mongo_db
import pymongo

database = mongo_db.connect()

def create_migration_register(migration_name, batch_id):
    database.migrations.insert_one({
        "migration": migration_name,
        "batch": batch_id
    })

def delete_migration_register(batch_id):
    database.migrations.delete_many({
        "batch": batch_id
    })

def check_file(migration_name):
    counter = database.migrations.find({
        "migration": migration_name
    }).count()

    if counter > 0:
        return False

    return True

def get_batch_id():
    last_register = list(database.migrations.find().sort("batch", pymongo.DESCENDING).limit(1))

    if len(last_register) == 0:
        return 1

    if len(last_register) > 0:
        return last_register[0]['batch'] + 1

def get_last_batch():
    last_register = list(database.migrations.find().sort("batch", pymongo.DESCENDING).limit(1))

    if len(last_register) == 0:
        return False

    if len(last_register) > 0:
        return last_register[0]['batch']


def get_files_from_last_batch():
    last_files = list(database.migrations.aggregate(
        [
            {
                "$group" :
                    {
                        "_id": "$batch",
                        "files": {"$addToSet": "$migration"},
                    },
            },
            {
                "$sort" : {"batch": -1}
            }
        ]
    ))

    if len(last_files) == 0:
        return False

    if len(last_files) > 0:
        return last_files[0]
