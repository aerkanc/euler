__author__ = 'Ahmet Erkan ÇELİK'
from datetime import datetime
import math

def get_share_item(n, d):
    for i in n:
        if i in d:
            return i
    return None

def div_by_share_digit(num, denom):
    n_digits = [int(i) for i in str(num)]
    d_digits = [int(i) for i in str(denom)]
    s = get_share_item(n_digits, d_digits)
    if s is not None:
        n_digits.remove(s)
        d_digits.remove(s)
        n = int(''.join(map(str,n_digits)))
        d = int(''.join(map(str,d_digits)))
        if d == 0:
            return None
        div = n / d
        return div
    return None

count = 0
startTime = datetime.now()
nums = 1
denoms = 1
for x in range(10, 100):
    for y in range(x+1, 100):
        if x % 10 == 0 and y % 10 == 0:
            continue
        div1 = div_by_share_digit(x, y)
        if div1 is None:
            continue
        div2 = x / y
        if div1 == div2:
            nums *= x
            denoms *= y
            count += 1
            print("%d / %d" % (x, y))

result = nums / denoms
print(result)
print(datetime.now()-startTime)



