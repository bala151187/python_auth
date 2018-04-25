from pymongo import MongoClient
import pymongo,logging,os
connectString = os.environ['MONGODB_wauth']
connection = MongoClient(connectString, connectTimeoutMS=5000)
auth_db = connection['auth']
collection = auth_db['users']
token=auth_db['tokens']
collection.insert_one({
  "email": "something@somewhere.com",
  "key": "abc",
  "secret": "abc"
})
token.insert_one({
 "token":"sadjhsadkasjdkja"
})
admin_db = connection['admin']
admin_db.add_user('accountUser', 'password', roles=[{'role':'readWrite','db':'admin'}])
