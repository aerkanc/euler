__author__ = 'Ahmet Erkan ÇELİK'

from datetime import datetime
import math

# The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
#
# Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.


startTime = datetime.now()
result = 0
for n in range(1, 1001):
    result += n ** n

print("Result is: %s" % (str(result)[-10:]))
print(datetime.now() - startTime)
exit()
