import string

__author__ = 'Ahmet Erkan ÇELİK'
from datetime import datetime
import math

def isPrime(x):
    if x < 2 : return False
    max = math.floor(math.sqrt(x))+1
    for n in range(2,max):
        if x % n == 0:
            return False
    else:
        return True

def primes(n = 2):
   while(True):
       if isPrime(n): yield n
       n += 1

def main():
    i=0
    for n in primes():
       i+=1
       if i==10001:
           print(n)
           return

if __name__ == "__main__":
    startTime = datetime.now()
    main()
    print(datetime.now()-startTime)
