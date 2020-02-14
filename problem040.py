__author__ = 'Ahmet Erkan ÇELİK'

from datetime import datetime
import math

startTime = datetime.now()

# https://projecteuler.net/problem=40
# An irrational decimal fraction is created by concatenating the positive integers:
#
# 0.123456789101112131415161718192021...
#
# It can be seen that the 12th digit of the fractional part is 1.
#
# If dn represents the nth digit of the fractional part, find the value of the following expression.
#
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

result = 1
d = 0
i = 0
irr_number_frac = ""
while d <= 1000000:
    i += 1
    irr_number_frac += str(i)
    d = len(irr_number_frac)

for r in range(0,6):
    result *= int(irr_number_frac[10 ** r - 1])
print(result)
print(datetime.now()-startTime)



