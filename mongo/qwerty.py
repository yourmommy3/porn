import pymongo

cli = pymongo.MongoClient('mongodb://localhost:27017')
db = cli["flask"]
collection=db["flak0"]
'''
dic = [
    {"name":"name1","add":"highway to 1hell"},
    {"name":"name2","add":"highway to h2ell"},
    {"name":"name3","add":"highway to he3ll"},
    {"name":"name4","add":"highway to hel4l"},
    {"name":"name5","add":"highway to hel5l"},
    {"name":"name6","add":"highway to 6hell"},
    {"name":"name7","add":"highway to 7hell"},
    {"name":"name8","add":"highway to 8cehell"}
]
x = collection.insert_many(dic)
'''
#for x in collection.find({},{'_id': 0, 'name': 'name1', 'add': 'highway to hell'}):
#    print(x)

#for x in collection.find():
#    print(x)
#collection.delete_one({"name":"name1"})

collection.update_one({"name":"name1"},{"$set":{"name":"satay"}})




for x in collection.find():
    print(x)