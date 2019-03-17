import datetime
now=datetime.datetime.now()
#print(now)
k=now.replace(microsecond=0)
print(k)