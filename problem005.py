import string

__author__ = 'Ahmet Erkan ÇELİK'
from datetime import datetime
import math
divisors = [11,13,14,15,16,17,18,19]
def isDivisable(n):
    for x in divisors:
        if n % x !=0:
            return False
    return True

def main():
    max=1
    for n in divisors:
        max*=n
    for n in range(20,max):
        if isDivisable(n):
            print(n)
            return

if __name__ == "__main__":
    startTime = datetime.now()
    main()
    print(datetime.now()-startTime)
