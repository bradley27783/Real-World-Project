
#
#
#
# IN THE DATE IN THE TIMETABLE -> MONTH IS INDEXED (JAN = 0, FEB = 1)
# start : new Date(blah blah blah) needs to become -> start : [blah blah blah]
#
#
import requests

import json
import demjson
import datetime
import ast
from bs4 import BeautifulSoup
from requests_ntlm import HttpNtlmAuth
from getpass import getpass


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
        if counter >= 388 and l.strip() != '':
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
    #close the dic here
    f.write("}")
    f.close()

    print("Loading...")
    jsFile = open("html.txt", "r")
    jsObj = jsFile.read()
    jsFile.close()
    pyObj = demjson.decode(jsObj)


    
    timetableDict = pyObj


    print(type(timetableDict))
    print(timetableDict["event0"]["start"][0])


    
    #NOW ONLY WRITE INTO TXT FILE, THE DATES UP TO a month
    #timetableDict[instance]["start"][?]
    #When ? is 0 = year, 1 = month - 1, 2 = day, 3 + 4 is time so dw
    #del timetableDict[instance]

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


    
    f = open("html.txt", "w")
    f.write(str(timetableDict))
    f.close()


    
    

    
def getTimetable(url):
    

    user = input('Enter your University login: ')
    password =   getpass('Now enter your password: ')

    print("Retrieving timetable")

    auth = HttpNtlmAuth('\\' + user, password)
    timetable = requests.get("https://webapp.coventry.ac.uk/Timetable-main/Timetable/Current/", auth=auth)

    if timetable.status_code == 200:
        print("Completed loading timetable!")
        format(timetable)
    elif timetable.status_code == 401:
        print("Incorrect username/password")
    else:
        print("Error! Status code: " + timetable.status_code)



getTimetable(timetable)
W8 = input()
