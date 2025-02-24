import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from custom_library import generate_array  

# Call the function 
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