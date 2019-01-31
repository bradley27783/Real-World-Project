# import web scraping libraries
import requests

timetable = "https://webapp.coventry.ac.uk/Timetable-main/Show/7658503?f=&t=&d=20170926&u=EEC/Timetable&k=aB7yw-TFnWGgPYLHzXDz8woGNts.X#view=agendaWeek"

    
    
def scrape(timetable):
    # query website and return the html
    page = requests.get(timetable)
    print(page.status_code) #200 means a ok :D
    
    
scrape(timetable)