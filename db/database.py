import pymongo
import pprint
import data
from bson.objectid import ObjectId
from bson.son import SON

# create client
myclient = pymongo.MongoClient('mongodb://localhost:27017')
# create database/name
mydb = myclient['database']
# my collection --> table equivalent
mycol = mydb["ECB"]  


# insert document to collection
post = mycol.posts
insert = post.insert_one(data.ecb)
insert = post.insert_one(data.library)


room_id = post.distinct("ECG.rid")
print(room_id)


'''
to get object ID:
  print(post.find_one({"building": "Lanchester libarary"}))
  print(post.find_one({"building": "Engineering and computing building (ECB)"}))

one of many ways
'''


# The web framework gets post_id from the URL and passes it as a string
# and thus parsing object ID as plain string fails.
# ECB ID

#pprint.pprint(post.find_one({'_id': ObjectId('5c5f05a784d3ce0a6abf3acb')}))
#print("\n\n\n")
# Lanchester Library ID
#pprint.pprint(post.find_one({'_id': ObjectId('5c5f07a984d3ce0ae52f1cdc')}))
