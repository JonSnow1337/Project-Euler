"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""
import math
import time
def isPrime(x):
    isPrime = True
    #try to divide it with all numbers between it and square root of it +1
    #square root because its impossible to divide with larger values
    #this brings great performance improvements(from 8 seconds to 0.11 secs in building a list to 10000)
    for number in xrange(2,int(math.sqrt(x)) + 1):
        if x % number == 0:
            isPrime = False
    return isPrime

def findPrimesBelowNumber(number):
    primeList = []
    p = 2 
    while True:
        if p > number:
            break
        if isPrime(p):
            primeList.append(p)
        p += 1
    return primeList
 
print sum(findPrimesBelowNumber(2000000))

