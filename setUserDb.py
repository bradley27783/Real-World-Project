'''
Issue no.1 : in userCol() - inefficiency with comparisons between usernames and key values stored in database


<RESOLVED> Issue no.2 : in userCol() - determining what the randomly generated salt number is for each password that gets salted+hashed
							if we can't, how will we make authentication comparisons ?

Issue no.3 : General flaw - what if a user changes his/her password on the coventry uni site ?
'''

import pymongo
from passlib.hash import pbkdf2_sha256
from pprint import pprint


# create/setup db client
myclient = pymongo.MongoClient('mongodb://localhost:27017')
mydb = myclient['database']
mycol = mydb['user-data']
post = mycol.posts


# for testing purpose: removes all documents 
def removeDocuments():
	post.delete_many({})  


# adds user-related documents to 'user-data' collection
def userCol(user, pwd):
	# Issue no.1
	for document in post.find({}):
		for data in sorted(dict.keys(document)):
			if user == data:
				if pbkdf2_sha256.verify(pwd, document[user]) == True:
					print("Success")
					return True
				else:
					print("Failure")
					return False
	# Issue no.2 <RESOLVED> <if pbkdf2_sha256.verify(pwd, document[user]) == True:>
	user_data = {user:pbkdf2_sha256.hash(pwd)}
	insert = post.insert_one(user_data)


# PoC to show documents in collection
def displayData():
	for document in post.find({}):
		pprint(document)


