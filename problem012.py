__author__ = 'Ahmet Erkan ÇELİK'
from datetime import datetime
import math
def divCount(number):
    counter=2
    i=2
    div=0
    while number/i != div:
        if number % i == 0:
            counter+=2
            if i*i == number:
                break
            div = i
        i+=1
    return counter
def main():
    number=28
    i=8
    max =0
    while max<500:
        dc = divCount(number)
        if max<dc:
            max = dc
            print(dc)
        number+=i
        i+=1
    print(number)

if __name__ == "__main__":
    startTime = datetime.now()
    main()
    print(datetime.now()-startTime)
