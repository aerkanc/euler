__author__ = 'Ahmet Erkan ÇELİK'
from datetime import datetime
import math


startTime = datetime.now()
primeCache = {}
def isDoublePalindrome(x):
    base2 ="{0:b}".format(x)
    return str(x) == str(x)[::-1] and str(base2) == str(base2)[::-1]

sum=0

for n in range(1,1000000):
    if isDoublePalindrome(n):
        sum += n

print(sum)
print(datetime.now()-startTime)



