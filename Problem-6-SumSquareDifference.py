"""
The sum of the squares of the first ten natural numbers is,

385
The square of the sum of the first ten natural numbers is,
3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""

def findSumSquares(rng):
    _sum = 0
    for num in xrange(1,rng + 1):
        _sum += num ** 2 
    return _sum

def findSquareSum(rng):
    _sum = 0
    for num in xrange(1, rng + 1):
        _sum += num
        
    return _sum ** 2

print findSquareSum(100) - findSumSquares(100)
