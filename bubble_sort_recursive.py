def bubble_sort(arr):
    """
    A sorting algorithm.
    
    Input: an array (here in Python, a list)
    Output: the array sorted
    Runtime Complexity: O^2
    """
    for i in range(0, len(arr) - 1):
        swapped = False
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            swapped = True
            bubble_sort(arr)
    return arr

print(bubble_sort.__doc__)
print(bubble_sort([2,52,42, 123, 9, 6, 3,2,1]))