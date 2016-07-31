__author__ = 'Ahmet Erkan ÇELİK'
from datetime import datetime
import math

def isPrime(x):
    if x < 2 : return False
    max = math.floor(math.sqrt(x))+1
    #print("==x=={}==MAX=={}".format(x,max))
    for n in range(2,max):
        #print("TEST {}".format(n))
        if x % n == 0:
            return False
    else:
        return True
def primes(n = 2,max=3):
   while(n < max):
       if isPrime(n): yield n
       n += 1

def main():
    result =0
    for n in primes(2,2000000):
        result+=n
    print(result)

if __name__ == "__main__":
    startTime = datetime.now()
    main()
    print(datetime.now()-startTime)
