"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342
(three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen)
contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.

"""

"""
How algorithm works:
    -first we build a list with strings for all numbers from 0 to 1000
    -then we just count up all the leters for all the numbers, not counting hyphens and spaces
"""
#i had no idea how to name these lists 
#im sorry
singles = ["one","two","three","four","five","six","seven","eight","nine"]
tens = ["ten", "eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
#Nones help us out here for future when we call  tys[2] we get twenty.
tys = [None,None,"twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety","cock"]

#builing first 19 numbers from hardcoded values in list
letterNumbers = ["zero"]
letterNumbers += singles
letterNumbers += tens

#now from 20 to 100
firstPart = None
for i in xrange(20,100):
    if i % 10 == 0:
        #just get tens values.
        letterNumbers.append(tys[i/10])
        firstPart = tys[i/10]
    else:
        #get tens value plus add singles value
        secondPart = singles [i % 10 - 1]
        letterNumbers.append(str(firstPart)+ "-" + (secondPart))
#from 100 to 1000
firstPart = None
for i in xrange(100,1000):
    if i % 100 == 0:
        #easy, just get tys values.
        letterNumbers.append(singles[i/100 - 1] + " hundred")
        firstPart = singles[i/100 - 1] + " hundred"
    else:
        #get tys values plus get last 2 numbers that we already know.
        letterNumbers.append(firstPart + " and " + letterNumbers[i % 100])

letterNumbers.append("one thousand")
#k lets count them up
count = 0
for num in letterNumbers[1:]:
    for letter in num:
        if letter not in (" ", "-"):
            count += 1
print count 
