"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

"""
Explenation:
First we get all the prime numbers in range of 2 to the number we're looking for.
Then we try to divide the number with all the primes, starting from the largest one.
When we find the number that divides it evenly, thats the largest prime

"""
import time
import math
def isPrime(x):
    isPrime = True
    #try to divide it with all numbers between it and square root of it +1
    #square root because its impossible to divide with larger values
    #this brings great performance improvements(from 8 seconds to 0.11 secs in building a list to 10000)
    for number in xrange(2,int(math.sqrt(x)) + 1):
        if x % number == 0:
            isPrime = False
    return isPrime

#creates a prime number list 
def getPrimeNumbersInRange(_range):
    return [number for number in xrange(2,_range) if isPrime(number)]
    

def getLargestPrimeFactor(num):
    #first get all the primes in range of num, reversed
    tStart = time.time()
    primeList = reversed(getPrimeNumbersInRange(int(math.sqrt(num))))
    print "it took", time.time() - tStart, " seconds to build the list"
    #find largest prime that divides it. 
    for prime in primeList:
        #print "dividing", num, "with", prime
        if num % prime == 0:
            return prime

print getLargestPrimeFactor(600851475143)
