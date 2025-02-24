import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from custom_library import generate_array  

# Call the function
arr = generate_array()  
print("UNSORTED ARRAY:", arr)


# Complexity: Time O(N^2) - Space 0(1)
def selection_sort(arr):

    # Iterate over array
    for i in range(len(arr)):
        min_index = i # assume current element is the smallest

        # find the smallest element in the remaining array
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j # update the smallest element index

        # Swap the current element with the smallest element found
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

print("SORTED ARRAY:  ", selection_sort(arr))