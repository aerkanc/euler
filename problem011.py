__author__ = 'Ahmet Erkan ÇELİK'
from datetime import datetime
import math
def divCount(number):
    counter=2
    target = number
    i=2
    while i <target:
        if number % i == 0:
            target /=i
            counter+=2
        i+=1
    return counter
def main():
    number=28
    i=8
    while divCount(number)<500:
        number+=i
        i+=1
    print(number)

if __name__ == "__main__":
    startTime = datetime.now()
    main()
    print(datetime.now()-startTime)
