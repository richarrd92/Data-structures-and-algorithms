import sys

# path to custom_functions
sys.path.append("/Users/richa/OneDrive/Documents/SCHOOL/CODING/DSA/custom_functions")

# Import the function directly
from generate_array import generate_array # type: ignore

# Call the function properly
arr = generate_array()  
print("UNSORTED ARRAY:", arr)


# Complexity: Time O(N log N) - Space O(N)
def merge(arr, low, mid, high):

    # Initialize pointers for both halves
    left_pointer = low       # Pointer for the left half
    right_pointer = mid + 1  # Pointer for the right half
    temp_arr = []            # Temporary array to store the merged result

    # Merge the two halves until one of them is exhausted
    while left_pointer <= mid and right_pointer <= high:
        if arr[left_pointer] <= arr[right_pointer]:
            # Append the smaller element from the left half
            temp_arr.append(arr[left_pointer])
            left_pointer += 1
        else:
            # Append the smaller element from the right half
            temp_arr.append(arr[right_pointer])
            right_pointer += 1

    # Copy any remaining elements from the left half
    while left_pointer <= mid:
        temp_arr.append(arr[left_pointer])
        left_pointer += 1

    # Copy any remaining elements from the right half
    while right_pointer <= high:
        temp_arr.append(arr[right_pointer])
        right_pointer += 1

    # Write the sorted elements back into the original array
    for i in range(low, high + 1):
        arr[i] = temp_arr[i - low]  # Map temp_arr indices back to the array



# Complexity: Time O(N log N) - Space O(N)
def merge_sort(arr, low, high):

    if low < high:
        # Calculate the middle index of the range
        mid = (low + high) // 2

        # Recursively sort the left half of the range
        merge_sort(arr, low, mid)

        # Recursively sort the right half of the range
        merge_sort(arr, mid + 1, high)

        # Merge the two sorted halves
        merge(arr, low, mid, high)
    
    return arr

print("SORTED ARRAY:  ", merge_sort(arr, 0, len(arr) - 1))