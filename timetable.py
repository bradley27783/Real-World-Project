#6591 - 6465 and 0 to 207
# # import web scraping libraries
# https://stackoverflow.com/questions/24027589/how-to-convert-raw-javascript-object-to-python-dictionary/26900181#26900181
# CHECK DISCORD
import requests
from bs4 import BeautifulSoup

timetable = "https://webapp.coventry.ac.uk/Timetable-main/Show/7658503?f=&t=&d=20170926&u=EEC/Timetable&k=aB7yw-TFnWGgPYLHzXDz8woGNts.X#view=agendaWeek"
#timetable = "https://webapp.coventry.ac.uk/Timetable-main/"
    
    
def scrape(timetable):
    # query website and return the html
    counter = 0
    s = requests.session()
    page = requests.get(timetable)
    
    print(page.status_code) #200 means a ok :D
    
    html = BeautifulSoup(page.content, 'html.parser')
    
    html = html.prettify() #<--dont do that again
    
    f = open("html.txt", "w")
    f.write(html)
    f.close()
    f = open("html.txt", "r")
    lines = f.readlines()
    f.close()    
    blaclist = ['ourEventId:', 'color:', 'mainColor', 'eventType:', 'sourceid:']
    blacklistCounter = 0
    f = open("html.txt", "w")
    for l in lines:
        if counter >= 202 and l.strip() != '': #and NOT USELESS LINES
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

    #html.txt now has in key : value pair - the data for each event in the timetable
    #now: https://stackoverflow.com/questions/24027589/how-to-convert-raw-javascript-object-to-python-dictionary/26900181#26900181
    f.close()
    
    



    
    
def getTimetable(url):
    

    payload = {'some': 'data'}

    r = requests.post(url, json=payload)
    r = requests.put(url, data = {'key':'value'})
    



#
#
scrape(timetable)
#getTimetable(timetable)
