import string

__author__ = 'Ahmet Erkan ÇELİK'
from datetime import datetime
import math


def main():
    for a in range(1,333):
        for b in range(a+1,math.floor((1000-a)/2)):
            c= 1000 - (a+b)
            if math.sqrt(a*a+b*b) == c:
                print(a*b*c)
                return

if __name__ == "__main__":
    startTime = datetime.now()
    main()
    print(datetime.now()-startTime)
