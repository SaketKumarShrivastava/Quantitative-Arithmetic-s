# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 18:59:24 2025

@author: SShrivastava9
"""

import math

# Function to calculate HCF of two numbers
def hcf(x, y):
    while y:
        x, y = y, x % y
    return x

# Function to calculate LCM of two numbers
def lcm(x, y):
    return abs(x * y) // hcf(x, y)

# Function to calculate HCF of an array of numbers
def hcf_of_array(arr):
    hcf_value = arr[0]
    for num in arr[1:]:
        hcf_value = hcf(hcf_value, num)
    return hcf_value

# Function to calculate LCM of an array of numbers
def lcm_of_array(arr):
    lcm_value = arr[0]
    for num in arr[1:]:
        lcm_value = lcm(lcm_value, num)
    return lcm_value

# Function to handle decimal inputs and find HCF and LCM
def hcf_lcm_decimal(arr):
    # Convert decimals to integers by finding the power of 10 required to remove decimals
    factor = 10 ** max([len(str(num).split('.')[1]) for num in arr])  # Find the max decimal places
    int_arr = [int(num * factor) for num in arr]
    
    # Calculate HCF and LCM for integers
    hcf_value = hcf_of_array(int_arr)
    lcm_value = lcm_of_array(int_arr)
    
    # Convert back to decimal by dividing by the factor
    hcf_decimal = hcf_value / factor
    lcm_decimal = lcm_value / factor
    
    return hcf_decimal, lcm_decimal

# Example usage
numbers = list(map(float, input("Enter decimal numbers separated by space: ").split()))

hcf_result, lcm_result = hcf_lcm_decimal(numbers)

print(f"The HCF of the decimal numbers is {hcf_result}")
print(f"The LCM of the decimal numbers is {lcm_result}")
