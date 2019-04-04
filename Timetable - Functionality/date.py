from datetime import date
import calendar


def getCurrentDay():
    my_date = date.today()
    return calendar.day_name[my_date.weekday()]