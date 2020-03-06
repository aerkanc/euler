__author__ = 'Ahmet Erkan ÇELİK'

from datetime import datetime
import math

#
# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
#
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
#
# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.

startTime = datetime.now()
result = 0


def is_featured(n):
    if len(str(int(n))) != 10:
        return False
    prime_numbers = {1: 2, 2: 3, 3: 5, 4: 7, 5: 11, 6: 13, 7: 17}
    for i, prime_number in prime_numbers.items():
        sub_number = int(n[i: i + 3])
        if sub_number % prime_number != 0:
            return False
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


def get_featured_pandigital_number():
    digits = ["9", "8", "7", "6", "5", "4", "3", "2", "1", "0"]
    for number in get_number(digits):
        # print("Generated Number: %s" % (number))
        if is_featured(number):
            yield int(number)


for n in get_featured_pandigital_number():
    # print(n)
    result += n

# print(is_featured('1406357289'))
# print(is_featured('4196357280'))
print("Result is: %s" % (result))
print(datetime.now() - startTime)
# Result is: 16695334890
# 0:00:09.803554
