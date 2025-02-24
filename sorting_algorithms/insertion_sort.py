import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from custom_library import generate_array 

# Call the function
arr = generate_array()  
print("UNSORTED ARRAY:", arr)


# Complexity: Time O(N^2) - Space O(1)
def insertion_sort(arr):

    # Iterate through the entire array starting from the second element
    for i in range(1, len(arr)):
        j = i
        # Compare and shift elements that are larger than the current element
        while j > 0 and arr[j] < arr[j - 1]:
            # Swap the elements to place the current element in the correct position
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j = j - 1

    # Return the sorted array
    return arr

print("SORTED ARRAY:  ", insertion_sort(arr))