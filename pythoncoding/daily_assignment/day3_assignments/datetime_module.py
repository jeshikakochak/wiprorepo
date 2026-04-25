#datetime module
import datetime
now=datetime.datetime.now()
print("current date and time:",now)
date1=datetime.date(2024,1,1)
date2=datetime.date(2024,12,31)
print("days between dates:",(date2 - date1).days)

print("formatted date:",now.strftime("%d-%m-%Y"))