# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 18:48:25 2025

@author: SShrivastava9
"""

def prime_factors_with_degrees(n):
    factors = {}
    
    # Check for the number of 2s in n
    while n % 2 == 0:
        if 2 in factors:
            factors[2] += 1
        else:
            factors[2] = 1
        n //= 2
    
    # Check for odd factors from 3 to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            if i in factors:
                factors[i] += 1
            else:
                factors[i] = 1
            n //= i
    
    # If n is a prime number greater than 2
    if n > 2:
        factors[n] = 1
    
    return factors

# Example usage
num = int(input("Enter a number: "))
factors = prime_factors_with_degrees(num)

print(f"Prime factorization of {num} is:")
for prime, degree in factors.items():
    print(f"{prime}^{degree}")
