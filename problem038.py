__author__ = 'Ahmet Erkan ÇELİK'

from datetime import datetime
import math


lg_pandig_num =0


def check_pandig(num):
    if str(num).__len__() != 9:
        return False
    for dig in range(1,9):
        if str(dig) not in str(num):
            return False
    return True

startTime = datetime.now()

for num in range(1, int(math.sqrt(987654321))):
    con = ""
    for d in range(1,9):
        mul = d * num
        con = con + str(mul)
        if con.__len__() > 9:
            break
        elif check_pandig(con) and int(con) > lg_pandig_num:
            lg_pandig_num = int(con)
            break
    else:
        continue

print(lg_pandig_num)
print(datetime.now()-startTime)



