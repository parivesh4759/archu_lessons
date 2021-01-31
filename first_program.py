from datetime import datetime
import time
from random import randint

odds = [1, 3, 5, 7, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 52, 53, 55, 57, 59]
i = 0
for i in range(5):
    right_this_minute = datetime.today().minute
    if right_this_minute in odds:
        print(right_this_minute)
        print("This minute seems a little odd.")
    else:
        print("Not an odd minute.")
    sec = randint(1, 60)
    time.sleep(sec)
