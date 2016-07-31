import string

__author__ = 'Ahmet Erkan ÇELİK'
from datetime import datetime
import math

def main():
   sumofsquare=0
   total=0
   for n in range(1,101):
       total+=n
       sumofsquare += n**2
   squareofsum = total**2
   print(squareofsum-sumofsquare)

if __name__ == "__main__":
    startTime = datetime.now()
    main()
    print(datetime.now()-startTime)
