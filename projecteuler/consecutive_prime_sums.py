'''
Created on May 10, 2016

@author: Bryan
'''
from math import sqrt, pow
from sys import argv
from time import time

'''
Determines whether or not an integer n is prime, given an ordered list of all positive
primes up to sqrt(n). Returns true if n is prime and false otherwise.
'''
def is_prime(n, primes):
    is_prime = True
    
    if n > 1:
        i = 0
        sqrt_n = sqrt(n)
        
        p = primes[0]
        while is_prime and i < len(primes) and p <= sqrt_n:
            if n % p == 0:
                # p | n or p > sqrt(n)
                is_prime = False
            else:
                i += 1
                p = primes[i]
    
    return is_prime

'''
Generates a list of lists of the parameter list li, with each list generated being of
the specified length and containing consecutive elements from the list li.
'''
def conseq_sequences(li, length):
    return [li[i:i + length] for i in range(0, len(li)) if len(li[i:i + length]) == length]

'''
Given a list of all primes at most n, this function generates a returns a sublist consisting
of smaller primes if n is too large.  That is, for large n, empirical data indicates that
reviewing primes that are less than floor(n/100) is sufficient for finding the longest
continuous subsequence of prime numbers that sum to a number less than n.
'''
def limited_prime_list(primes, n):
    limit = n
    
    if n >= 100000:
        limit = n // 100
    
    return [primes[i] for i in range(0, len(primes)) if primes[i] < limit]
                
'''
Given a set of primes and list of primes up to the given sum_limit, this
function finds a sublist of consecutive_prime_summands of maximum size whose sum
is a prime number.  It returns this sublist.
''' 
def find_longest_subsequence(prime_set, prime_list, sum_limit):
    max_prime_summand_subseq = []
    
    l = len(prime_list)  # length of subsequence
    while not(max_prime_summand_subseq) and l > 0:
        cons_prim_summand_subseq_list = conseq_sequences(prime_list, l)
        
        for subseq in cons_prim_summand_subseq_list:
            sum_subseq = sum(subseq)
        
            if sum_subseq < sum_limit and sum_subseq in prime_set:
                max_prime_summand_subseq = subseq
                break
            
        l -= 1
    
    return max_prime_summand_subseq

'''
Demo and test function
'''
if __name__ == "__main__":
    d = 2
    
    if len(argv) > 1:
        d = int(argv[1])
    
    n = int(pow(10, d))
    n = 100
    
    while n <= 1000000:
        for i in range(0,1):
            start_time = time()
            
            primes = [2]    # list used because ordering is important in search
            
            for x in range(3, n):
                if is_prime(x, primes):
                    primes.append(x)
            
            prime_set = set(primes) # checking for element containment is faster with a set
            prime_list = limited_prime_list(primes, n)
            
            elapsed_time = time() - start_time
            
            print(n, len(primes), elapsed_time)
            
            start_time = time()
            
            max_prime_summand_subseq = find_longest_subsequence(prime_set, prime_list, n)
            
            elapsed_time = time() - start_time
            
            print(n, max_prime_summand_subseq, len(max_prime_summand_subseq), sum(max_prime_summand_subseq), elapsed_time)
            
            n *= 10
                
        
        
                       
