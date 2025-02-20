import sys

# path to custom_functions
sys.path.append("/Users/richa/OneDrive/Documents/SCHOOL/CODING/DSA/custom_functions")

# Import the function directly
from generate_array import generate_array # type: ignore

# Call the function properly
arr = generate_array()  
print("UNSORTED ARRAY:", arr)


# Complexity: Time O(N + K) - Space O(N + K) -> K = Buckets
def bucket_sort(arr):
    
    # Find the maximum value in the array to determine the bucket range
    max_value = max(arr)
    bucket_count = len(arr) # Number of buckets
    bucket_range = (max_value + 1) / bucket_count # Range of each bucket

    # Create empty buckets
    buckets = [[] for _ in range(bucket_count)]

    # Place each element in its corresponding bucket
    for num in arr:
        index = int(num / bucket_range) # Calculate the bucket index
        buckets[index].append(num)

    # Sort each bucket and concatenate them
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket)) # Concatenate sorted buckets

    return sorted_arr

print("SORTED ARRAY:  ", bucket_sort(arr))