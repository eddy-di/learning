from datetime import datetime
import time

dt1 = datetime(2023, 4, 8) # prints given time
dt = datetime.now() # prints recent time
dt3 = datetime.strptime("2022/08/31", "%Y/%m/%d") # prints time from string parsing it from string
dt4 = datetime.fromtimestamp(time.time()) # similar as line 5 but using time module


print(f"{dt.month}/{dt.year}")
print(dt.strftime("%m/%Y"))

print(dt3 > dt1)