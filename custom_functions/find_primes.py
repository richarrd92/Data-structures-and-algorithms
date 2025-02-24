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
    
print(find_primes(10))