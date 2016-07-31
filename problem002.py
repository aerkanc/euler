__author__ = 'Ahmet Erkan ÇELİK'
from datetime import datetime
def main():
    f0,f1,total=1,1,0
    while f1<4000000:
        f0,f1=f1,f0+f1
        if f0 % 2 ==0:
            total+=f0
    print(total)
if __name__ == "__main__":
    startTime = datetime.now()
    main()
    print(datetime.now()-startTime)
