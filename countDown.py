__author__ = 'Minotaurus'
def countdown(start,last):
    n=start
    while(n>last):
        yield n
        n-=1

for n in range(10,0,-1):
    print(n)
