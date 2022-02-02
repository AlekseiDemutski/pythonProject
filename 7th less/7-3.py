import datetime

d = datetime.date(2020, 1, 15)
print(d)
print(type(d))

today = datetime.date.today()
print(today)
print(type(today))

print(today - d)
print(type(today - d))