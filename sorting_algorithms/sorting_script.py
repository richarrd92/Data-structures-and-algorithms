import random # generate random numbers
import argparse # parse command-line arguments

# Generate array of random integers
def generate_array(size, max_value):
    return [int(random.random() * max_value) for _ in range(size)]



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



# Main function
if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Sort an array using the specified algorithm.")
    parser.add_argument("algorithm", choices=["selection", "bubble", "insertion", "merge", "bucket"], help="Sorting algorithm to use.")
    parser.add_argument("size", nargs="?", type=int, default=10, help="Number of elements in the array (default: 10).")
    parser.add_argument("max_value", nargs="?", type=int, default=100, help="Maximum value of elements in the array (default: 100).")
    args = parser.parse_args()

    # Generate array and sort it
    arr = generate_array(args.size, args.max_value)
    
    # Print the unsorted array
    if args.algorithm == "selection":
        print("SELECTION SORT: ")
        print(f"Unsorted -> {arr}")
        sorted_arr = selection_sort(arr)
    elif args.algorithm == "bubble":
        print("BUBBLE SORT: ")
        print(f"Unsorted -> {arr}")
        sorted_arr = bubble_sort(arr)
    elif args.algorithm == "insertion":
        print("INSERTION SORT: ")
        print(f"Unsorted -> {arr}")
        sorted_arr = insertion_sort(arr)
    elif args.algorithm == "merge":
        print("MERGE SORT: ")
        print(f"Unsorted -> {arr}")
        sorted_arr = merge_sort(arr, 0, len(arr) - 1)
    elif args.algorithm == "bucket":
        print("BUCKET SORT: ")
        print(f"Unsorted -> {arr}")
        sorted_arr = bucket_sort(arr)

    print(f"Sorted ->   {sorted_arr}") # Print the sorted array