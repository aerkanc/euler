from math import sqrt
from datetime import datetime
startTime = datetime.now()
prime = lambda x:False if [i for i in range(2,int(sqrt(x)+1)) if x%i==0] else True
n = 2
c = 0
while c < 10001:
    if prime(n):
        p=n
        c+=1
    n+=1
print(p)
print(datetime.now()-startTime)