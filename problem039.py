__author__ = 'Ahmet Erkan ÇELİK'

from datetime import datetime
import math

startTime = datetime.now()

# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
# there are exactly three solutions for p = 120.
# {20,48,52}, {24,45,51}, {30,40,50}
# For which value of p ≤ 1000, is the number of solutions maximised?


def is_right_angle_triangle(a, b, c):
    sides = [a,b,c]
    sides.sort()
    c = sides[2]
    b = sides[1]
    a = sides[0]
    if (c > a + b) or (a < c - b) or (c**2 != a**2 + b**2): return False
    return True
sol = {}
limit = 1000
max_p = 0
max_s = 0
for p in range(3, limit):
    limit_a = int(p / 3) + 1
    for a in range(1, limit_a):
        limit_b = int((p - a)/2) + 1
        for b in range(a, limit_b):
            c = p - (a + b)
            if is_right_angle_triangle(a, b, c):
                if p in sol:
                   sol[p] += 1
                else:
                   sol[p] = 1
                if max_s < sol[p]:
                    max_p = p
                    max_s = sol[p]

print("Result is: ", max_p, max_s)
print(datetime.now()-startTime)



