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
    m = math.floor(math.sqrt(x)) + 1
    for n in range(2, m):
        if x % n == 0:
            return False
    else:
        return True


def get_number(number_pool):
    if len(number_pool) == 1:
        for d in number_pool:
            yield d
    else:
        for start_index in range(0, len(number_pool)):
            d = number_pool[start_index]
            new_number_pool = []
            for n in number_pool:
                if n != d:
                    new_number_pool.append(n)
            for n in get_number(new_number_pool):
                if n is not None:
                    yield d + n
                start_index += 1
                if start_index >= len(new_number_pool):
                    start_index = 0


def get_prime_pandigital_number():
    digits = ["9", "8", "7", "6", "5", "4", "3", "2", "1"]
    digit_num = len(digits)
    for dn in range(digit_num, 1, -1):
        pool = digits[digit_num-dn:]
        for number in get_number(pool):
            print("Generated Number: %s" % (number))
            if is_prime(int(number)):
                return number


print("Result is: ", get_prime_pandigital_number())
print(datetime.now() - startTime)
# Result is:  7652413
# 0:00:01.572953