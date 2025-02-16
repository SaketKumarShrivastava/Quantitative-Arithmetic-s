# Function to calculate HCF of two numbers
def hcf(x, y):
    while y:
        x, y = y, x % y
    return x

# Function to calculate LCM of two numbers
def lcm(x, y):
    return abs(x * y) // hcf(x, y)

# Function to calculate HCF of a list of numbers
def hcf_of_array(arr):
    hcf_value = arr[0]
    for num in arr[1:]:
        hcf_value = hcf(hcf_value, num)
    return hcf_value

# Function to calculate LCM of a list of numbers
def lcm_of_array(arr):
    lcm_value = arr[0]
    for num in arr[1:]:
        lcm_value = lcm(lcm_value, num)
    return lcm_value

# Input: array of numbers
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Calculate HCF and LCM of the array
hcf_result = hcf_of_array(numbers)
lcm_result = lcm_of_array(numbers)

# Display the results
print(f"The HCF of the array is {hcf_result}")
print(f"The LCM of the array is {lcm_result}")
