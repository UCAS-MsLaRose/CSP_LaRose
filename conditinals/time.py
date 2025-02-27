#Vienna LaRose, How to get the time of day

import time
#first instance of time in programming
#print(time.gmtime())

#current time in seconds since gmtime
current =time.time()

#Current time as we are used to seeing it
now = time.ctime(current)
print(now)

#get just the hour
local_time = time.localtime(current)
hour = local_time.tm_hour
minute = local_time.tm_min
print(hour)