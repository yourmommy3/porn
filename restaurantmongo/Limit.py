import pymongo
connection_url="mongodb://localhost:27017/"
client=pymongo.MongoClient(connection_url)
database_name="Restaurant"
Restaurant=client[database_name]
collection_name="Customer"
collection=Restaurant[collection_name]
limit5=collection.find().limit(5)
for data in limit5:
    print(data)