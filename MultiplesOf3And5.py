"""If we list all the natural numbers below 10 that are multiples of 3 or 5
, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

#kind of a lame way to do it
"""_sum = 0
for number in range(1000):
    if number % 5 == 0 or number % 3 == 0:
        sum += number 

print _sum"""


#kind of a cool way to do it.
x = [number for number in xrange(1000) if number % 3 == 0 or number % 5 == 0]
print sum(x) 
