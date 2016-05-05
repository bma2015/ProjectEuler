'''
Created on May 4, 2016

@author: Bryan
'''
from sys import argv

'''
Obtains the digits of a number in decimal format for the number in the base expansion
'''
def get_digits(num, base):
    digits = []
    quotient = num
    remainder = 0
    
    while (quotient > 0):
        remainder = quotient % base
        digits.append(remainder)
        quotient = quotient // base
        
    return digits        

'''
Obtains the digits of the given number in the base expansion.  Returns true if the ith and
(n-i)th digits in the expansion are the same.
'''
def is_palindrome(num, base):
    digits = get_digits(num, base)
    
    is_palindrome = True
    i = 0
    num_digits = len(digits)
    while i < num_digits and is_palindrome:
        if digits[i] != digits[num_digits - i - 1]:
            is_palindrome = False
        i += 1
        
    return is_palindrome
    
if __name__ == "__main__":
    n = 1000000
    
    if len(argv) > 1:
        n = int(argv[1])
    
    palindrome_sum = 0
    
    for i in range(0,n+1):
        if (is_palindrome(i,10) and is_palindrome(i,2)):
            palindrome_sum += i
    
    print(palindrome_sum)