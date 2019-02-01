# import web scraping libraries
import requests

from bs4 import BeautifulSoup

timetable = "https://webapp.coventry.ac.uk/Timetable-main/Show/7658503?f=&t=&d=20170926&u=EEC/Timetable&k=aB7yw-TFnWGgPYLHzXDz8woGNts.X#view=agendaWeek"
#timetable = "https://webapp.coventry.ac.uk/Timetable-main/Timetable/Current#view=agendaWeek"
    
    
def scrape(timetable):
    # query website and return the html
    page = requests.get(timetable)
    
    print(page.status_code) #200 means a ok :D
    
    html = BeautifulSoup(page.content, 'html.parser')
    
    print(html.prettify()) #<--dont do that again
    


    
    
def getTimetable(url):
    
    password = input("Enter password ")
    data = {
    'username': 'mcgeevej',
    'password': password
     }


    page = requests.post(url, data=data)
    html = BeautifulSoup(page.content, 'html.parser')
    
    print(html.prettify())
    


#
scrape(timetable)
#getTimetable(timetable)
