def selection_sort(arr):
    """
    An inefficent algorithm for many real-word data sets. 
    Input: array
    Output: sorted arr
    Runtime: O(n^2)
    """
    for i in range (0, len(arr) - 1):
        smallest = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

print(selection_sort.__doc__)
print(selection_sort([12,33,42, 1213, 39, 26, 3,23,1]))