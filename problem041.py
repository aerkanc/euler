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
    m = math.floor(math.sqrt(x))+1
    for n in range(2, m):
        if x % n == 0:
            return False
    else:
        return True


def get_number(start_index, number_pool):
    d = number_pool[start_index]
    new_number_pool = []
    for n in number_pool:
        if n != d:
            new_number_pool.append(n)
    if len(new_number_pool) == 0:
        return d
    start_index +=1
    if start_index >= len(new_number_pool):
        start_index = 0
    return d + get_number(start_index,new_number_pool)


def get_prime_pandigital_number():
    digits = ["9","8","7","6","5","4","3","2","1"]
    digit_num = len(digits)
    for dn in range(digit_num, 1, -1):
        pool = digits.copy()[digit_num-dn:dn]
        for i in range(0, dn):
            number = get_number(i, pool)
            if is_prime(int(number)):
                return number

print("Result is: ", get_prime_pandigital_number())
print(datetime.now()-startTime)



