'''
Issue no.1 : in userCol() - inefficiency with comparisons between usernames and key values stored in database


<RESOLVED> Issue no.2 : in userCol() - determining what the randomly generated salt number is for each password that gets salted+hashed
							if we can't, how will we make authentication comparisons ?

Issue no.3 : General flaw - what if a user changes his/her password on the coventry uni site ?

Issue no.4 : in userCol() Timetable on login:
	# this part of the code verifies user/pass. It has nothing to do with
	# the timetable, which could be a problem later. Because IF a user exists in the db
	# it returns right away.
'''

import pymongo
from passlib.hash import pbkdf2_sha256
from pprint import pprint

# issues with html.txt
f = open("html.txt")

# create/setup db client
myclient = pymongo.MongoClient('mongodb://localhost:27017')
mydb = myclient['database']
mycol = mydb['user-data']
post = mycol.posts


# for testing purpose: removes all documents 
def removeDocuments():
	post.delete_many({})  

# test code
def skipTimetable(user):
	for document in post.find({}):
		for data in sorted(dict.keys(document)):
			if user == data:
				return True
	return False

# adds user-related documents to 'user-data' collection
def userCol(user, pwd, optional=0):
	print("[DEBUG] DB 1")
	# Issue no.1

	for document in post.find({}):
		for data in sorted(dict.keys(document)):
			if user == data:
				print("-------------")
				print(data)
				print(user)
				print("------------")
				# --- Issue no.4 ---
				# verifies user+password
				#print("------------------")
				#print(document[user][0]['password'])
				#print("------------------")
				if pbkdf2_sha256.verify(pwd, document[user][0]['password']) == True:					
					print("[DEBUG] CORRECT PASSWORD")
					return True
				else:
					print("Failure")
					return False
	
	user_data = {user:[{"password":pbkdf2_sha256.hash(pwd)}, {"timetable":f.read()}]} # for now takes user/pass - but should also store timetable info.
	insert = post.insert_one(user_data)
	# Issue no.2 <RESOLVED> <if pbkdf2_sha256.verify(pwd, document[user]) == True:>
	return True


# PoC to show documents in collection
def displayData():
	for document in post.find({}):
		pprint(document)


#removeDocuments()
displayData()

