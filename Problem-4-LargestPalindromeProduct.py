"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 X 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
#first cast the num to string, reverse it and see if its the same
def isPalindrome(num): 
    strNum = str(num)
    reversedNum =strNum[ : : -1]
    return reversedNum == strNum

def findLargestPalindrome(length):
    largestPalindrome = 0
    for i in range(length):
        for j in range(length):
            if isPalindrome(i * j):
                palindrome = i * j
                if palindrome > largestPalindrome:
                    largestPalindrome = palindrome
    return largestPalindrome

print findLargestPalindrome(999) 
