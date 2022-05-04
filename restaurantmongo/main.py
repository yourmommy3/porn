from gc import collect
import pymongo
connection_url="mongodb://localhost:27017/"
client=pymongo.MongoClient(connection_url)
database_name="Restaurant"
Restaurant=client[database_name]
collection_name="Customer"
collection1=Restaurant[collection_name]
foodcust=[
   {"Foodname":"Dal tadka","Price":159,"Quantity":"1","Rating":"4"},
   {"Foodname":"Paneer 65","Price":169,"Quantity":"1","Rating":"5"},
   {"Foodname":"Paneer paratha","Price":60,"Quantity":"4","Rating":"4"},
   {"Foodname":"Mushroom masala","Price":179,"Quantity":"1","Rating":"5"},
   {"Foodname":"Veg kofta","Price":139,"Quantity":"1","Rating":"3"}
]
collection1.insert_many(foodcust)
collection_name="Foodid"
collection2=Restaurant[collection_name]
foodid=[
   {"FoodId":1,"Foodname":"Dal tadka"},
   {"FoodId":2,"Foodname":"Paneer 65"},
   {"FoodId":3,"Foodname":"Paneer Paratha"},
   {"FoodId":4,"Foodname":"Mushroom masala"},
   {"FoodId":5,"Foodname":"Veg kofta"}
]
collection2.insert_many(foodid)
for data in collection1.find().sort("Price"):
   print(data)

for data in collection2.find():
   print(data)

