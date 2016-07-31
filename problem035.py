__author__ = 'Ahmet Erkan ÇELİK'
from datetime import datetime
import math


startTime = datetime.now()
primeCache = {}
def isPrime(x):
    if x in  primeCache.keys():
        return primeCache[x]
    if x < 2 : return False
    max = math.floor(math.sqrt(x))+1
    #print("==x=={}==MAX=={}".format(x,max))
    for n in range(2,max):
        #print("TEST {}".format(n))
        if x % n == 0:
            primeCache[x] = False
            return False
    else:
        primeCache[x]=True
        return True

circularPolarList = [2]
nonCircularPolarList = []

for n in range(3,1000000,2):
    if n not in circularPolarList and n not in nonCircularPolarList:
        n_digits = [int(i) for i in str(n)]
        allRotationsPrime = True
        rotations={}
        for i in range(0,len(n_digits)):
            if n_digits[i] in [0,2,4,5,6,8]:
                allRotationsPrime = False
                break
            x_digits = []
            for j in range(i,i+len(n_digits)):
                x_digits.append(n_digits[j % len(n_digits)])
            number = int(''.join(map(str,x_digits)))
            rotations[number]= True
            if not isPrime(number):
                allRotationsPrime = False
                break
        if allRotationsPrime:
            for number in rotations.keys():
                circularPolarList.append(number)
                print("%d => %d" % (n,number))
        else:
            for number in rotations.keys():
                nonCircularPolarList.append(number)


print(len(circularPolarList))
print(datetime.now()-startTime)



