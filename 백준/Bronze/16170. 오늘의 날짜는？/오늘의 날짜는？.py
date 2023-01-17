import datetime

utc_time = datetime.datetime.utcnow()

print(utc_time.year)
print(str(utc_time.month).rjust(2,'0'))
print(str(utc_time.day).rjust(2,'0'))