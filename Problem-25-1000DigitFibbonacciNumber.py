# -*- coding: utf-8 -*-

"""The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?"""

def fib():
    f1 = 1
    f2 = 1
    while True:
        yield f1+f2
        f1,f2 = f2, f1+f2


def getNumOfDigits(num):
    strNum = str(num)
    return len(strNum)

index = 2 #my function actually starts from 3rd fib number
for fibNumber in fib():
    index += 1
    if getNumOfDigits(fibNumber) == 1000:
        print index
        break
