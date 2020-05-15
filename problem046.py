__author__ = 'Ahmet Erkan ÇELİK'

from datetime import datetime
import math

# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
#
# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2
#
# It turns out that the conjecture was false.
#
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

primes = []

def is_prime(x):
    if x < 2:
        return False
    m = math.floor(math.sqrt(x)) + 1
    for n in range(2, m):
        if x % n == 0:
            return False
    else:
        return True


def is_square(number):
    sqrt = math.sqrt(number)
    return int(sqrt) == sqrt


def has_goldbach_conjecture(number):
    if is_prime(number):
        return False
    if number % 2 == 0:
        return False
    for i in range(1, number):
        if is_prime(i) and (number-i) % 2 == 0 and is_square((number-i)/2):
            return True
    return False


n = 9
while has_goldbach_conjecture(n):
    n += 2
    while is_prime(n):
        n += 2


startTime = datetime.now()
result = n


print("Result is: %s" % (result))
print(datetime.now() - startTime)
exit()

