
#https://projecteuler.net/problem=26
from decimal import *
import re
def removeZeroes(s):
    p = re.compile('0\\.0*(\d+)')
    m = p.match(s)
    return m.group(1)

def findRepeatingPattern(s):
    p = re.compile('(\d+)\\1+')
    m = p.match(s)
    if m == None:
        return 0
    pattern =  m.group(1)
    while True:
        if pattern is not None:
            oldPattern = pattern
            pattern = p.match(str(pattern))
            if pattern is not None:
                pattern = pattern.group(1)
            if pattern == None:
                pattern = oldPattern
                break
    return pattern

getcontext().prec = 5000
maxReccuring = 0
d = 0
for i in xrange(2,1000):
    num = Decimal(1)/Decimal(i)
    num = removeZeroes(str(num))
    pattern = findRepeatingPattern(num)
    if len(str(pattern)) > maxReccuring:
        d = i
        maxReccuring = len(str(pattern))

print "largest reciprocal number d for 1/d is ", d


