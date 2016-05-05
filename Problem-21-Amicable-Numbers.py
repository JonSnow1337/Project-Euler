# -*- coding: utf-8 -*-
"""
Let d(n) be defined as the sum of proper divisors of
n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b
are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
Evaluate the sum of all the amicable numbers under 10000.
"""

def d(n):
    #sum of proper divisors of n
    _sum = 0
    iterationEnd = n/2 + 1
    for i in xrange(1,iterationEnd):
        if n % i  == 0:
            _sum += i
    return _sum


def getAmicableNumberSum(range):
    _sum = 0
    for i in xrange(1,range):
        a = d(i)
        b = d(a)
        if b == i and b != a:
            _sum += a + b
            print a, " ", b
            print _sum
    #divide by 2 because we add pairs twice
    #this way we dont waste ram :)
    #and im lazy
    return _sum / 2

print (getAmicableNumberSum(10000))






