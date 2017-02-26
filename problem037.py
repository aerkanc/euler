__author__ = 'Ahmet Erkan ÇELİK'

from datetime import datetime
import math
primeCache = {}


def is_prime(x):
    if x in  primeCache.keys():
        return primeCache[x]
    if x < 2 : return False
    max = math.floor(math.sqrt(x))+1
    for n in range(2, max):
        if x % n == 0:
            primeCache[x] = False
            return False
    else:
        primeCache[x]=True
        return True


def is_trunc_prime(n, v):
    if n < 10:
        return is_prime(n)
    if is_prime(n):
        if v == "left":
           n = int(str(n)[1:])
        else:
           n = int(str(n)[:-1])
        return is_trunc_prime(n, v)
    return False


def is_both_trunc_prime(n):
    return is_trunc_prime(n, "left") and is_trunc_prime(n, "right")

startTime = datetime.now()

truncPrimeNumber = 0
truncPrimes = []
sum =0
number = 11
while truncPrimeNumber < 11:
    if is_both_trunc_prime(number):
        sum += number
        truncPrimeNumber += 1
        truncPrimes.append(number)
    number += 1

print(sum)
print(truncPrimes)
print(datetime.now()-startTime)



