def binary_search_recursive(arr, target):
    """
    A recursive implementaion of binary search. Precondition: array must be sorted. Finding if a item exists in a list
    Input: Array, target value
    Output: Value's index or false
    Runtime Complexity: O(log(n))
    """
    low = 0
    high = len(arr) - 1
    midpoint = (high + low) // 2

    if target == arr[midpoint]:
        return midpoint
    elif target > arr[midpoint]:
        return binary_search_recursive(arr[midpoint:], target)
    elif target < arr[midpoint]:
        return binary_search_recursive(arr[:midpoint], target)
    else:
        return false


print(binary_search_recursive.__doc__)
print(binary_search_recursive([1,2,3,4,5,6,7,8,9], 5))
print(binary_search_recursive([1,2,3,4,5,6,7,8,9], 2))
print(binary_search_recursive([1,2,3,4,5,6,7,8,9], 10))