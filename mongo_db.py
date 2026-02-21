from pymongo import MongoClient

def insert_into_mongo(data):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["market_trend_db"]
    collection = db["consumer_data"]

    collection.insert_many(data)

    print("Data inserted into MongoDB successfully.")