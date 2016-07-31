__author__ = 'Ahmet Erkan ÇELİK'
from datetime import datetime
import math
coins =[200,100,50,20,10,5,2,1]

target = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
ways = [1] + [0]*target

startTime = datetime.now()
for coin in coins:
    for i in range(coin, target+1):
        ways[i] += ways[i-coin]

print("Ways to make change = %d", ways[target])
print(datetime.now()-startTime)
