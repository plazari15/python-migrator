from database_connector import mongo_db
import pymongo

database = mongo_db.connect()

def create_migration_register(migration_name, batch_id):
    database.migrations.insert_one({
        "migration": migration_name,
        "batch": batch_id
    })

def get_batch_id():
    last_register = database.migrations.find().sort("batch", pymongo.DESCENDING).limit(1)[0]

    if last_register is not None:
        return last_register['batch'] + 1
