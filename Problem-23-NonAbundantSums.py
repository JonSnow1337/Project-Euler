"""A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example,

the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum
exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two
abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written
as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it
is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

import os
import pickle

def findProperDivisors(number):
    properDivisors = []
    for i in xrange(1,number/2 + 1):
        if number % i == 0:
            properDivisors.append(i)
    return properDivisors

def isAbundant(number):
    divisors = findProperDivisors(number)
    return sum(divisors) > number

def getAbundantNumbers(limit):
    ret = []
    for i in xrange(limit):
        if isAbundant(i):
            ret.append(i)

    return ret

def getSummableNumbers(abundantNumbers):
    summables = set()
    #using set to not have duplicates in the list
    #i guess theres a better way to find sums by somehow excluding possible duplicates
    #not sure how

    for index,i in enumerate(abundantNumbers):
        for j in abundantNumbers[index:]:
            if i + j >=28123:
                break

            summables.add(i + j)

    return summables

#this was pretty slow so i made it so it saves it.
#takes about 10 seconds i think
if os.path.isfile("./resources/abundantNums.txt"):
    with open("./resources/abundantNums.txt") as file:
        nums = pickle.loads(file.read())
else:
    nums = getAbundantNumbers(28123)
    with open("./resources/abundantNums.txt", "w+") as file:
        pickle.dump(nums, file)

canBeSummable = getSummableNumbers(nums)

result = 0
for i in xrange(28123):
    if i not in canBeSummable:
        result += i

print result



