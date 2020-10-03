__author__ = 'Ahmet Erkan ÇELİK'

from datetime import datetime
import math

# The first two consecutive numbers to have two distinct prime factors are:
#
# 14 = 2 × 7
# 15 = 3 × 5
#
# The first three consecutive numbers to have three distinct prime factors are:
#
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
#
# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?


startTime = datetime.now()
result = 0
primes = []


def is_prime(x):
    if x in primes:
        return True

    if x < 2:
        return False
    m = math.floor(math.sqrt(x)) + 1
    for n in range(2, m):
        if x % n == 0:
            return False
    else:
        primes.append(x)
        return True


consecutive_numbers = []
n = 999
while len(consecutive_numbers) < 4:
    n += 1
    prime_factors = []
    for f in range(2, n):
        if n % f == 0 and is_prime(f) and f not in prime_factors:
            prime_factors.append(f)
            if len(prime_factors) > 4:
                continue
    if len(prime_factors) == 4 and (len(consecutive_numbers) == 0 or consecutive_numbers[-1] + 1 == n):
        consecutive_numbers.append(n)
        print("%d is consecutive number as four distinct prime factors [%s]" % (
            n, ",".join(str(e) for e in prime_factors)))
    else:
        consecutive_numbers = []

result = consecutive_numbers[0]

print("Result is: %s" % (result))
print(datetime.now() - startTime)
exit()
