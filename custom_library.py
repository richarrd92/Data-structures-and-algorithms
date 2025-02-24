# IMPLEMENTATION OF CUSTOM FUNCTIONS - TO MIMIC A LIBRARY

import random # generate random numbers

# Generate array of random integers
def generate_array(size=15, max_value=10):
    return [int(random.random() * max_value) for _ in range(size)]

# returns list in reverse
def convert_binary_reverse(n: int) -> list:
    remainder = n%2 # stores the remainder
    binary_arr = [remainder]

    division_result = n // 2 # integer division
    if division_result == 0:
        return [remainder]
    
    return binary_arr + convert_binary_reverse(division_result)


# returns list of binary digits in order
def convert_binary(n: int) -> list:
    if n == 0:
        return [0]
    if n == 1:
        return [1]
    
    return convert_binary(n // 2) + [n % 2] # concatenation of both lists 

# given a number in integer form
# returns a list of prime numbers up to number
def find_primes(n: int) -> list:
    if n < 2:
        return []
    
    # Initialize list where index represents the number
    nums = [i for i in range(n + 1)]
    
    # Mark primes using Sieve of Eratosthenes
    for i in range(2, int(n**0.5) + 1):
        if nums[i] != 0:  # If number is still prime
            j = i * i  # Start marking from i^2
            while j <= n:
                nums[j] = 0  # Mark as non-prime
                j += i  # Increment by step of i
    
    # Collect non-zero values which are primes
    return [num for num in nums[2:] if num != 0]
    
# functions to match patterns -> not optimal 
def match_pattern(text: str, subpattern: str) -> dict:
    # empty subpattern string
    if not subpattern:
        return {"Empty subpattern" : [-1, -1]}  # Return no match for empty pattern
        
    text_length = len(text)
    subpattern_length = len(subpattern)
    text_index = 0
    subpattern_index = 0


    while text_index < text_length:  # Iterate through the main text
        # Attempt to match the pattern
        while subpattern_index < subpattern_length and text_index < text_length:
            if text[text_index] == subpattern[subpattern_index]:
                text_index += 1
                subpattern_index += 1  # Move forward in both text and pattern
            else:
                subpattern_index = 0  # Reset pattern index on mismatch
                break

        if subpattern_index == subpattern_length:  # Full pattern matched
            return {f"Match \"{subpattern}\" found": [text_index - subpattern_length, text_index - 1]}  # Return match start & end indices

        text_index += 1  # Move to the next character in the text
        
    return {f"No match \"{subpattern}\" found" : [-1, -1]} # No match found

# IMPLEMENT ONE TO RETURN ALL MATCHES 


