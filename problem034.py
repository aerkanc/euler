__author__ = 'Ahmet Erkan ÇELİK'
from datetime import datetime
import math


startTime = datetime.now()
total =0
factorials = []


def prepare():
    for i in range(0,10):
        factorials.insert(i,math.factorial(i))


def sum_of_facts(number):
    n_digits = [int(i) for i in str(number)]
    sum =0
    for d in n_digits:
        sum += factorials[d]
    if sum == number:
        return number
    return 0
prepare()
for n in range(10,2540161):
    total += sum_of_facts(n)

print(total)
print(datetime.now()-startTime)



