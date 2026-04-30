import time
'''
try:
    while True:
        current=(time.strftime("%I:%M:%S %p"))
        print(f" {current}", end="\r")
        time.sleep(1)
except KeyboardInterrupt:
    print("\nClock stopped.\n")
'''

import time 
my_time=int(input("Enter the time in seconds: "))
for x in range(my_time,0,-1):
    seconds=x%60
    minutes=int(x/60)%60
    hours=int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}", end="\r")
    time.sleep(1)
print("Times UP!")