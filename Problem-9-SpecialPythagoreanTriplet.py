"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a **2 + b ** 2 = c **22
For example, 3 **2 + 4 **2 = 9 + 16 = 25 = 5 ** 2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import math 
for a in range(1000):
    for b in range(1000):
        c = a **2 + b **2
        c = math.sqrt(c)
        if a < b < c and c.is_integer() and a + b +c == 1000:
            print a,b,c
            print a*b*c
