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

def getLargestPrimeFactorOLD(num):
    #first get all the primes in range of num, reversed
    tStart = time.time()
    primeList = reversed(getPrimeNumbersInRange((num)))
    print "it took", time.time() - tStart, " seconds to build the list"
    #find largest prime that divides it. 
    for prime in primeList:
        #print "dividing", num, "with", prime
        if num % prime == 0:
            return prime
#print getLargestPrimeFactor(600851475143)
print getLargestPrimeFactor(600851475143)
