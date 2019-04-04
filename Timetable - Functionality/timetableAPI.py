import sqlite3

def format_Timetable(timetable):
    timetableDict = {}
    time = ["09:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00"]
    for lesson in timetable:
        for hour in time:
            if lesson[0] == hour:
                if hour in timetableDict:
                    timetableDict[hour].append(lesson)
                else:
                    timetableDict[hour] = [lesson]

    return timetableDict

def fetch_timetable(username):
    conn = sqlite3.connect('timetableDB.db')
    cur = conn.cursor()
    timetable = cur.execute('''SELECT * FROM timetable
                            WHERE user_id = ?;''',(username,))
    
    return format_Timetable(timetable.fetchall())    

#print(fetch_timetable(1))

def format2(timetable):
    time = ["09:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00"]
    timeValue = {"09:00":"9","10:00":"10","11:00":"11","12:00":"12","13:00":"13","14:00":"14","15:00":"15","16:00":"16","17:00":"17","18:00":"18"}
    days = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
    daysValue = {"Monday":'mon',"Tuesday":'tue',"Wednesday":'wed',"Thursday":'thu',"Friday":'fri'}
    
    timetableDict = {}
    for lesson in timetable:
        for hour in time:
            if lesson[0] == hour:
                print(lesson)
                hour_diff = int(timeValue[lesson[1]])-int(timeValue[lesson[0]])
                lesson_id = daysValue[lesson[2]]+timeValue[lesson[0]]+"h"+str(hour_diff)
                if lesson_id in timetableDict:
                    timetableDict[lesson_id].append(lesson)
                else:
                    timetableDict[lesson_id] = [lesson]
    return timetableDict

def fetch_timetable2(username):
    conn = sqlite3.connect('timetableDB.db')
    cur = conn.cursor()
    timetable = cur.execute('''SELECT * FROM timetable
                            WHERE user_id = ?;''',(username,))
    
    return format2(timetable.fetchall())




#print(lesson_Id_Gen())

#print(fetch_timetable2(1))

"""
def website_Test(timetable):
    
    days = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
    times = ["09:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00"]
    scheduleTimes = ["09:00 - 10:00",
                    "10:00 - 11:00",
                    "11:00 - 12:00",
                    "12:00 - 13:00",
                    "13:00 - 14:00",
                    "14:00 - 15:00",
                    "15:00 - 16:00",
                    "16:00 - 17:00",
                    "17:00 - 18:00",
                    "18:00 - 19:00"]
    count = 0
    
    for time in times:
        print(scheduleTimes[count])
        for day in days:
            found = False
            print(f"\n{time} - {day}\n")
            if time in timetable:
                
                lessonFound = None
                for lesson in timetable[time]:
                    
                    if day in lesson:
                        found = True
                        lessonFound = lesson
                #print(found)
                if found:
                    print(f"{lessonFound}")
                    print(f"TIME {times[count]}")
                    print(count)
                    if count <= 7:
                        if lessonFound[1] == times[count+2]:
                            print(f"TWO HOUR - {lessonFound[1]} - {times[count+2]}")
                        else:
                            print("One Hour")
                else:
                    print("<td></td>")
            else:
                print("<td></td>")

        print("CLOSE")
        count += 1
website_Test(fetch_timetable(1))
"""



def format3(timetable):
    
    timeValue = {"09:00":"9","10:00":"10","11:00":"11","12:00":"12","13:00":"13","14:00":"14","15:00":"15","16:00":"16","17:00":"17","18:00":"18"}
    
    timetableDict = {}
    for lesson in timetable:
        lessonList = list(lesson)
        hourDiff = int(timeValue[lesson[1]])-int(timeValue[lesson[0]])
        lessonList.append(hourDiff)
        timeRange = lessonList[0] + " - " + lessonList[1]
        lessonList.append(timeRange)
        
        
        if lessonList[2] in timetableDict:
            timetableDict[lessonList[2]].append(lessonList)
        else:
            timetableDict[lessonList[2]] = [lessonList]
    
    #for val in timetableDict:
        #print(val + "\n" + str(timetableDict[val]))
        
    return timetableDict
        
        
def fetch_timetable3(username):
    conn = sqlite3.connect('timetableDB.db')
    cur = conn.cursor()
    timetable = cur.execute('''SELECT * FROM timetable
                            WHERE user_id = ?;''',(username,))
    
    return format3(timetable.fetchall())


print(fetch_timetable3(1))