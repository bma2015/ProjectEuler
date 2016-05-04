'''
Created on Jan 9, 2016

@author: Bryan
'''
from math import sqrt, floor

'''
Checks if a number is prime.  Returns True if the number is prime and false otherwise.
'''
def is_prime(num, primes):
    if num > 1:
        sqrt_num = floor(sqrt(num))
        i = 0
        while (i < len(primes) and primes[i] <= sqrt_num):
            if num % primes[i] == 0:
                return False
            i += 1
        return True
    else:
        return False
    
'''
Generate the first primes within [1, 1000^2 + 1000*1000 + 1000].
'''
def populate_primes():
    primes = []
    for i in range(1,2001001):
        if is_prime(i,primes):
            primes.append(i)
    return primes

'''
Returns x^2 + ax + b
'''
def quadratic_prime(a, b, x):
    return x*x + a*x + b

'''
Generates a set of primes from a quadratic expression x^2 + ax + b
'''
def generate_quadratic_primes(a, b, primes):
    #print("x^2 +", a, "x +", b)  
    generated_primes = set()
    num = quadratic_prime(a, b, 0)
    i = 1
    while is_prime(num, primes):
        generated_primes.add(num)
        num = quadratic_prime(a, b, i)
        i += 1
    return generated_primes

if __name__ == "__main__":
    primes = populate_primes()
    max_a = -1
    max_b = -1
    max_list = []
    for i in range(-1000, 1001):
        for j in range(-1000, 1001):
            generated_primes = generate_quadratic_primes(i, j, primes)
            if (len(generated_primes) > len(max_list)):
                max_a = i
                max_b = j
                max_list = generated_primes
    print(len(max_list))
    print(max_a*max_b)