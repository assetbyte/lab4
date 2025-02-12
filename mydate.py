#1

from datetime import datetime,timedelta
today = datetime.today()
print(today - timedelta(days=5))

#2

todayy = datetime.today()
yesterday = todayy - timedelta(days=1)
tommorow = today + timedelta(days=1)
print("Today:", todayy)
print("Yesterday:", yesterday)
print("Tommorow:", tommorow)


#3

date_without_ms = datetime.now().replace(microsecond=0)
print(date_without_ms)

#3 2nd variant

todayyy = datetime.today()
print(todayyy.strftime("%x") + " " +  todayyy.strftime("%X"))

#4

date1 = datetime(2024, 2, 10, 12, 30, 15) 
date2 = datetime(2024, 2, 12, 14, 45, 30)  


difference = (date2 - date1).total_seconds()

print("Difference in seconds:", difference)