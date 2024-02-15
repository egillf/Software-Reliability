# (i)
def quicksort(array):
    # Sorts an array using the quicksort algorithm.
    # Returns a sorted array.

    # if the array has one element or is empty, it is already sorted
    if len(array) <= 1:
        return array
    
    # choose the pivot as the middle element
    pivot = array[len(array) // 2]

    # Partition the array into elements less than, equal to, and greater than the pivot
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]

    # Recursively sort the left and right partitions and concatenate the results
    return quicksort(left) + middle + quicksort(right)

# (ii)
def binary_search(array, target):
    # Performs binary search on a sorted array to find the target element.
    # returns True if target is found, False otherwise.

    left = 0
    right = len(array) - 1

    # Continue the search until the left pointer is greater than the right pointer
    while left <= right:
        mid_element = (left + right) // 2  # Find the middle element

        if array[mid_element] == target:
            return True  # Target found, returns true
        elif array[mid_element] < target:
            left = mid_element + 1  # Adjust the left pointer
        else:
            right = mid_element - 1  # Adjust the right pointer

    return False  # Target not found

# (iii)
def sort_and_search(array, elem):
    # combines (i) and (ii)
    arr_copy = quicksort(array.copy())  # Make a copy of the array and sort it
    return binary_search(arr_copy, elem)  # Perform binary search on the sorted array

### MUTATIONS ###

# MUTATION 1: Mutating Quicksort Base Case
def m1_quicksort(array):
    if len(array) <= 2: # <-- mutated, original: if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# MUTATION 2: Mutate Pivot Selection
def m2_quicksort(array):
    if len(array) <= 1:
        return array
    pivot = array[0] # <-- mutated, original: pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# MUTATION 3: Mutate Binary Search Comparison
def m3_binary_search(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid_element = (left + right) // 2 
        if array[mid_element] <= target: # <-- mutated, original: array[mid_element] == target
            return True
        elif array[mid_element] < target:
            left = mid_element + 1
        else:
            right = mid_element - 1
    return False

# MUTATION 4: Mutate Binary Search Adjustment
def m4_binary_search(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid_element = (left + right) // 2 
        if array[mid_element] == target:
            return True
        elif array[mid_element] < target:
            left = mid_element + 1
        else:
            right = mid_element # <-- mutated, original: right = mid_element - 1

# MUTATION 5: Mutate Binary Search Exit Condition
def m5_binary_search(array, target):
    left = 0
    right = len(array) - 1
    while left < right: # <-- mutated, original: while left <= right
        mid_element = (left + right) // 2 
        if array[mid_element] == target:
            return True
        elif array[mid_element] < target:
            left = mid_element + 1
        else:
            right = mid_element  

# MUTATION 6: Integration Error: Reverse Sorted Array
def m6_sort_and_search(array, elem):
    arr_copy = quicksort(array.copy())
    arr_copy.sort(reverse=True) # <-- mutated, array sorted in the opposite order
    return binary_search(arr_copy, elem) 