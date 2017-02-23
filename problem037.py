__author__ = 'Ahmet Erkan ÇELİK'

from datetime import datetime
import math
primeCache = {}
def isPrime(x):
    if x in  primeCache.keys():
        return primeCache[x]
    if x < 2 : return False
    max = math.floor(math.sqrt(x))+1
    for n in range(2,max):
        if x % n == 0:
            primeCache[x] = False
            return False
    else:
        primeCache[x]=True
        return True


startTime = datetime.now()

primeDigits = [2, 3, 5, 7]
primeIndex = 0
truncPrimeCache = []
sum =0
while primeIndex<11:
    for d in primeDigits:
        p = d
        tp = p
        while isPrime(tp):
            for o in range(1, 9):
                if tp > 10 and truncPrimeCache.index(tp) == -1:
                    p = tp
                    truncPrimeCache.append(tp)
                    primeIndex += 1
                    sum += p
                tp = int(str(o)+ str(p))

print(sum)
print(datetime.now()-startTime)



