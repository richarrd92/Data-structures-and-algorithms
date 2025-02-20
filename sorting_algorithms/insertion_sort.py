import sys

# path to custom_functions
sys.path.append("/Users/richa/OneDrive/Documents/SCHOOL/CODING/DSA/custom_functions")

# Import the function directly
from generate_array import generate_array # type: ignore

# Call the function properly
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