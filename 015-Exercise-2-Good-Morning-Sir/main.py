# import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)

# if(int(time.strftime('%H') < 12) and (int(time.strftime('%H') >= 1))):
#     print("Good Morning")
# elif(int(time.strftime('%H') > 12) and (int(time.strftime('%H') < 19))):
#     print("Good Afternoon")
# else:
#     print("Good Night")


# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime


import datetime

timestamp = datetime.datetime.now().strftime('%H:%M:%S')
print(timestamp)

current_hour = datetime.datetime.now().hour

if 1 <= current_hour < 12:
    print("Good Morning")
elif 12 <= current_hour < 19:
    print("Good Afternoon")
else:
    print("Good Night")
