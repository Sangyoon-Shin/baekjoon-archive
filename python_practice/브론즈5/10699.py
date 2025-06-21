import datetime as dt

x = dt.datetime.now()
year = x.year
month = x.month
day = x.day

print(str(year) + '-' + '0'+str(month) + '-' + '0' + str(day))