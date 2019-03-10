import requests

from setUserDb import *

import json
import demjson
import datetime
import ast
from bs4 import BeautifulSoup
from requests_ntlm import HttpNtlmAuth
from getpass import getpass

# edit so it's not console-like app

timetable = "https://webapp.coventry.ac.uk/Timetable-main/"

def formatDate(oldDate):
    newDate = oldDate.replace("new Date", "")
    newDate = newDate.replace("(","[")
    newDate = newDate.replace(")","]")
    return newDate
    
def format(timetable):
    # query website and return the html
    counter = 0
    eventCounter = 0
    numOfLines = 0
    startReading = False
    html = BeautifulSoup(timetable.content, 'html.parser')
    f = open("html.txt", "w")
    f.write(str(html))
    f.close()
    f = open("html.txt", "r")
    lines = f.readlines()
    f.close()
    blaclist = ['ourEventId:', 'color:', 'mainColor', 'eventType:', 'sourceid:']
    blacklistCounter = 0
    f = open("html.txt", "w")
    #something to make it a dic opening here
    f.write("{")

    for l in lines:
        if startReading == True and l.strip() != '':
            if ": new Date(" in l: #formats the date entry to be able to convert into python
                l = formatDate(l)
                f.write(l)
                continue       
            if "{}" in l:
                break
            if "{" in l:
                f.write("event" + str(eventCounter) + " : {\n")
                eventCounter = eventCounter + 1
                continue
            if blaclist[blacklistCounter] in l:
                blacklistCounter = blacklistCounter + 1
                if blacklistCounter == 5:
                    blacklistCounter = 0
                continue
            f.write(l)
        counter = counter+1
        if "events: [" in l:
            startReading = True
    #close the dic here
    f.write("}")
    f.close()

    #print("Loading...")
    jsFile = open("html.txt", "r")
    jsObj = jsFile.read()
    jsFile.close()
    timetableDict = demjson.decode(jsObj)


    monthView = formatMonth(eventCounter, timetableDict)


    f = open("html.txt", "w")
    f.write(str(monthView))
    f.close()



def formatMonth(eventCounter, timetableDict):
    currentDate = datetime.date.today()

    
    for event in range(eventCounter):
        instance = "event" + str(event)
        if currentDate.month != 11 : #if not half way through december
            if timetableDict[instance]["start"][0] == currentDate.year: #if the year is correct
                if timetableDict[instance]["start"][1] + 1 == currentDate.month and timetableDict[instance]["start"][2] >= currentDate.day:
                   #if the month is the same as the events and the day is the same as today or above, then dont keep the instance
                     continue
                elif timetableDict[instance]["start"][1] == currentDate.month and timetableDict[instance]["start"][2] <= currentDate.day:
                   #if the instances month is one month more than the current month and the day is less than the todays day
                     continue
        else:
            if timetableDict[instance]["start"][0] == currentDate.year or timetableDict[instance]["start"][0] == currentDate.year + 1: #if year is this or next
                if timetableDict[instance]["start"][1] + 1 == currentDate.month and timetableDict[instance]["start"][2] >= currentDate.day:
                   #if the month is the same as the events and the day is the same as today or above, then dont keep the instance
                     continue
                elif timetableDict[instance]["start"][1] == 0 and timetableDict[instance]["start"][2] <= currentDate.day:
                   #if the instances month is 0 (jan) and the day is less than the todays day
                     continue
        del timetableDict[instance]


    return timetableDict
    

    
def getTimetable(username, password, url):
    
    print("[DEBUG] REACHED HERE - 1")
    #user = input('Enter your University login: ')
    #password =   getpass('Now enter your password: ')

    #print("Retrieving timetable")
    if skipTimetable(username) == True:
        if userCol(username, password) == True:
            print("[debug] REACHED HERE - 4")
            return True

    auth = HttpNtlmAuth('\\' + username, password)
    timetable = requests.get("https://webapp.coventry.ac.uk/Timetable-main/Timetable/Current/", auth=auth)

    if timetable.status_code == 200:
        print("[DEBUG] REACHED HERE - 3")
        format(timetable)
        if userCol(username, password) == True:
            print("[debug] REACHED HERE - 4")
            return True

        #print("Completed loading timetable!")
    elif timetable.status_code == 401:
        return False
        # show some error on web

        #print("Incorrect username/password")
    else:
        return False
        # show some error on the web

        #print("Error! Status code: " + timetable.status_code)

# return at status code ... 
# if code is 200, then add to db.
# store db so that flask can connect to it
# make it so that users can login depending on the credentials of the db

#W8 = input("DONE")
