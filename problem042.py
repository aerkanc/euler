__author__ = 'Ahmet Erkan ÇELİK'

from datetime import datetime
import math

startTime = datetime.now()

# https://projecteuler.net/problem=42
# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.
#
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?


def is_triangle_number(n):
    y = n * 2
    s = int(math.sqrt(y))
    d = y / s
    if math.fabs(d-s) == 1:
        # print("%s * %s / 2 = %s" % (s, d, n))
        return True
    return False

words = open("./data/42/p042_words.txt").read().replace("\"","").split(",")
letters = {}

for li in range(0, ord('Z')-ord('A') + 1):
    letters[chr(ord('A')+li)] = li+1
tw_count = 0
for w in words:
    wp = 0
    for l in w:
        wp += letters[l]
    # print('%s = %s' % (w, wp))
    if is_triangle_number(wp):
        tw_count+=1

print("Result is: %s" % (tw_count))
print(datetime.now() - startTime)
# Result is: 162
# 0:00:00.001681