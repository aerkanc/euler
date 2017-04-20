__author__ = 'Ahmet Erkan ÇELİK'
from datetime import datetime


def main():
    total = 0
    for n in range(3,1000):
        if n % 3 == 0 or n % 5 == 0:
            total+=n

    print(total)
if __name__=="__main__":
    startTime = datetime.now()
    main()
    print(datetime.now()-startTime)
