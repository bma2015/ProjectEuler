'''
Created on Jan 9, 2016

@author: Bryan
'''

'''
Calculates the power a^b of an integer a and a nonnegative integer exponent b.  Returns the result.
'''
def int_power(base, power):
    product = 1
    for i in range(1, power+1):
        product *= base
    return product

'''
Calculates the power sum 1^1 + 2^2 + 3^3 + ... n^n.  Returns the result.
''' 
def self_power_sum(n):
    sum = 0
    for i in range(1,n+1):
        sum += int_power(i,i)
    return sum

if __name__ == "__main__":
    result_str = str(self_power_sum(1000))
    last_digits = result_str[-10:]
    print(last_digits)