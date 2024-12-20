import random # generate random numbers

# Generate array of random integers
def generate_array():
    arr = [int(random.random() * 100) for i in range(10)]
    return arr

# Complexity: Time O(N^2) - Space 0(1)
def selection_sort():
    print("\nSELECTION SORT: ")
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

print(selection_sort())

print()
