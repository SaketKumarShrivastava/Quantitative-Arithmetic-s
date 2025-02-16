# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 18:34:38 2025

@author: SShrivastava9
"""

#The following method utilize the Sieve of Eratoshenes for the check

import math

# Function to generate a list of primes up to a given limit using Sieve of Eratosthenes
def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)  # Boolean array indicating primality
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime
    for start in range(2, int(math.sqrt(limit)) + 1):
        if sieve[start]:
            for multiple in range(start*start, limit + 1, start):
                sieve[multiple] = False
    return sieve

# Function to check if numbers in an array are prime
def check_primes(arr):
    max_value = max(arr)
    sieve = sieve_of_eratosthenes(max_value)  # Generate primes up to the maximum number
    return [sieve[num] for num in arr]

# Example usage:
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
results = check_primes(numbers)

for num, is_prime in zip(numbers, results):
    print(f"{num} is {'prime' if is_prime else 'not prime'}")
