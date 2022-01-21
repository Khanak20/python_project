import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017')
print(client)

# databases list --------------------
db_list = client.list_database_names()
print(db_list)

# create database --------------------
database = client['NewDB1'] 
print(database)

# create Collection --------------------
collect = database['Table1']
print(collect)

# Insert Record To Collection
dict1 = {'nm':'Darpan','em':'darpan@gmail.com','no':'123456789'}
collect.insert_one(dict1)

