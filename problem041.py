__author__ = 'Ahmet Erkan ÇELİK'

from datetime import datetime
import math

startTime = datetime.now()

# https://projecteuler.net/problem=41
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?

result = 1


def is_prime(x):
    if x < 2:
        return False
    max = math.floor(math.sqrt(x))+1
    for n in range(2, max):
        if x % n == 0:
            return False
    else:
        return True

digits = [0,1,2,3,4,5,6,7,8,9]


print("Result is: ", result)
print(datetime.now()-startTime)



