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

def getPrime(primeNum):
    primeFound = False
    p = 2 
    currentPrimeNum = 1
    while not primeFound:
        p += 1
        if isPrime(p):
            currentPrimeNum += 1
        if currentPrimeNum == primeNum:
            break
    return p
   
print getPrime(10001) 
