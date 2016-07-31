__author__ = 'Ahmet Erkan ÇELİK'
from datetime import datetime
import math



def is_pandigital_mul(x,y):
    mul = x * y
    x_digits = [int(i) for i in str(x)]
    y_digits = [int(i) for i in str(y)]
    mul_digits = [int(i) for i in str(mul)]
    all = x_digits + y_digits + mul_digits
    if all.__len__() != 9 or 0 in all:
        return 0
    for i in range(1,10):
        if i not in all:
            return 0
    print("%s x %s = %s" % (x,y,mul))
    return mul


startTime = datetime.now()
products =[]
total =0
first=[{"start":1,"end":10},{"start":10,"end":100}]
second=[{"start":1000,"end":10000},{"start":100,"end":1000}]
for s in range(0,2):
    for i in range(first[s]["start"],first[s]["end"]):
        for j in range(second[s]["start"],second[s]["end"]):
            mul = is_pandigital_mul(i,j)
            if mul != 0:
                products.append(mul)
total = sum(set(products))
print(total)
print(datetime.now()-startTime)
