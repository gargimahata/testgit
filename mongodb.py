import pymongo
client = pymongo.MongoClient("mongodb+srv://gargi4u:gargi4u@cluster0.oza10tb.mongodb.net/?retryWrites=true&w=majority")
db = client.test

d = {'name':'gargi',
     'saurnme':'mahata',
     'mail':'g@gmail.com'}

d = {'name':'gargi',
     'saurnme':'mahata',
     'mail':'g@gmail.com'}

d = {'name':'gargi',
     'saurnme':'mahata',
     'mail':'g@gmail.com'}

db1= client['mongotest']
coll = db1['test']
coll.insert_one(d )