import pymongo
from sensor.constant.database import DATABASE_NAME

class MongoDBClient:
    clent=None


    def __init__(self, database_name= DATABASE_NAME) -> None:
        try:
            if MongoDBClient.Client is None:
                mongo_db_url="mongodb+srv://oscartandi171:8Gnar0uKkEcRH6Wm@mongosensor.hq9cx19.mongodb.net/"
                MongoDBClient.client=pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client=MongoDBClient.client
            self.database = self.clie4nt[database_name]
            self.dataase_name= database_name
        except Exception as e:
            raise e