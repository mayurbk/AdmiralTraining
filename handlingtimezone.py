from datetime import datetime
import pytz

local_time = datetime.now()
print("Local Time is:",local_time.strftime("%m/%d/%Y, %H:%M:%S"))

tz_NY = pytz.timezone('America/New_York')
dt_NY = datetime.now(tz_NY)
print("NewYork time is:",dt_NY.strftime("%m/%d/%Y, %H:%M:%S"))



