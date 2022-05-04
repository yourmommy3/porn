import pymongo 
con = pymongo.MongoClient("localhost:27017")
database_name = "LAB1"
lab1 = con[database_name]
collection_name = "more"
con1 = lab1[collection_name]
lst = [
    {"index":"1","name":"a"},
    {"index":"2","name":"b"},
    {"index":"3","name":"c"}
]

con1.insert_many(lst)
cur = con1.find()

for i in cur:
    print(i)