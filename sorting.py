import random # generate random numbers

# Generate array of random integers
def generate_array():
    arr = [int(random.random() * 100) for i in range(10)]
    return arr

# Complexity: Time O(N^2) - Space 0(1)
def selection_sort():
    print("SELECTION SORT: ")
    arr = generate_array()
    print('Unsorted -> {}'.format(arr))
    
    # Iterate over array
    for i in range(len(arr)):
        min_index = i # assume current element is the smallest

        # find the smallest element in the remaining array
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j # update the smallest element index

        # Swap the current element with the smallest element found
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return 'Sorted ->   {}'.format(arr)


# Complexity: Time O(N^2) - Space O(1)
def bubble_sort():
    print("BUBBLE SORT: ")
    arr = generate_array()
    print('Unsorted -> {}'.format(arr))

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
    return 'Sorted ->   {}'.format(arr)


# Complexity: Time O(N^2) - Space O(1)
def insertion_sort():
    print("INSERTION SORT: ")
    arr = generate_array()
    print('Unsorted -> {}'.format(arr))

    # Iterate through the entire array starting from the second element
    for i in range(1, len(arr)):
        j = i
        # Compare and shift elements that are larger than the current element
        while j > 0 and arr[j] < arr[j - 1]:
            # Swap the elements to place the current element in the correct position
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j = j - 1

    # Return the sorted array
    return 'Sorted ->   {}'.format(arr)


print(insertion_sort())
