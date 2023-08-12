# A python program capable of greeting you with Good Morning, Good Afternoon and Good Evening.

import time                               # Importing time module
timestamp = time.strftime('%H:%M:%S')
print(timestamp)

hour = int(time.strftime('%H'))

if(hour>=0 and hour<12):                  # Using nested if-else
  print("Good Morning Sir!")
elif(hour>=12 and hour<17):
  print("Good Afternoon Sir!")
elif(hour>=17 and hour<24):
  print("Good Night Sir!")