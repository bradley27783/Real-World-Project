#6591 - 6465 and 0 to 207
# # import web scraping libraries
# https://stackoverflow.com/questions/24027589/how-to-convert-raw-javascript-object-to-python-dictionary/26900181#26900181
# CHECK DISCORD
import requests
from bs4 import BeautifulSoup
from requests_ntlm import HttpNtlmAuth
from getpass import getpass


timetable = "https://webapp.coventry.ac.uk/Timetable-main/"
    
    
def format(timetable):
    # query website and return the html
    counter = 0
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
    for l in lines:
        if counter >= 387 and l.strip() != '':
            if "]" in l:
                f.write(l)
                break
            if blaclist[blacklistCounter] in l:
                blacklistCounter = blacklistCounter + 1
                if blacklistCounter == 5:
                    blacklistCounter = 0
                continue
            f.write(l)
        counter = counter+1
    f.close()

    #html.txt now has in key : value pair - the data for each event in the timetable
    #now: https://stackoverflow.com/questions/24027589/how-to-convert-raw-javascript-object-to-python-dictionary/26900181#26900181
    
    
    



    
    
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