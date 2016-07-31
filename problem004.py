import string

__author__ = 'Ahmet Erkan ÇELİK'
from datetime import datetime
import math

def isPalindromic(n):
    strn = str(n)
    return strn == strn[::-1]

def main():
    largestPalindrome=0
    number = 0
    for f in range(99,999):
        for n in range(99,999):
            number = n * f
            if isPalindromic(number) and largestPalindrome<number:
                largestPalindrome = number
    print(largestPalindrome)
if __name__ == "__main__":
    startTime = datetime.now()
    main()
    print(datetime.now()-startTime)
