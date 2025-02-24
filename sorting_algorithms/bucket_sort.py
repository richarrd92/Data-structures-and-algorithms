import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from custom_library import generate_array

# Call the function
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