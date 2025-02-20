import sys

# path to custom_functions
sys.path.append("/Users/richa/OneDrive/Documents/SCHOOL/CODING/DSA/custom_functions")

# Import the function directly
from generate_array import generate_array # type: ignore

# Call the function properly
arr = generate_array()  
print("UNSORTED ARRAY:", arr)


# Complexity: Time O(N^2) - Space O(1)
def bubble_sort(arr):

    # Iterate through the entire array
    for i in range(len(arr)):
        swapped = False  # Keep track of whether any swaps occurred in this pass

        # Compare adjacent elements up to the unsorted portion
        for j in range(len(arr) - i - 1): 
            if arr[j] > arr[j + 1]:
                # Swap if elements are out of order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # Mark that a swap has occurred

        # If no swaps occurred during the pass, the array is already sorted - break out of loop
        if not swapped:
            break 
    
    # Return the sorted array after all passes are complete
    return arr

print("SORTED ARRAY:  ", bubble_sort(arr))