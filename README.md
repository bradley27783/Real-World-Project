# RealWorldProject

follow this guide to install mongodb on linux
----------------------------------------------------------------
https://docs.mongodb.com/v3.2/tutorial/install-mongodb-on-linux/

# Start mongo server
$ mongod


# requirements for user and password on mongodb:
timetable.py - collects user + password, and more
setUserDb.py - takes user + password, salts+hashes, stores in database. Only one instance of a user can exist... (a few issues noted in code)


# testing 
you can simply edit setUserDb.py and call displayData() function to see results in console.

$ python3 timetable.py
Enter your University login: 
Now enter your password: 


