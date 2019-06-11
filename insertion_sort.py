def insertion_sort(arr):
    """
    An efficient algorithm for sorting small arrays (here in python, lists).

    Input: a list of numbers l
    Output: list l sorted from smallest to largest
    Runtime complexity: O(n^2)
    """
    for i in range(1, len(arr)):
        num = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > num:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = num
    return arr

print(insertion_sort.__doc__)
print(insertion_sort([10,9,6,4,1,2,11,25,3]))
