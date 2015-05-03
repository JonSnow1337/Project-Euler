"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""



def largestNumberDivisbleTo(num):
    foundNum = False    
    targetNum = num 
    while not foundNum:
        for i in xrange(1, num + 1):
            if targetNum % i == 0:
                foundNum = True
                continue 
            else:
                targetNum += 1
                foundNum = False
                break
    return targetNum


print largestNumberDivisbleTo(20) 
