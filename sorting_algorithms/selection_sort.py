import sys

# path to custom_functions
sys.path.append("/Users/richa/OneDrive/Documents/SCHOOL/CODING/DSA/custom_functions")

# Import the function directly
from generate_array import generate_array # type: ignore

# Call the function properly
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