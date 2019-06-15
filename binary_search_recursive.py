def binary_search_recursive(arr, target, low, high):
    """
    A recursive implementaion of binary search. Precondition: array must be sorted. Finding if a item exists in a list
    Input: Array, target value
    Output: Value's index or false
    Runtime Complexity: O(log(n))
    """
    middle = (low + high) // 2

    if len(arr) == 0:
        return False
    
    if target > arr[-1]: 
        return False
    if target < arr[0]:
        return False

    if arr[middle] == target:
        return middle
    elif target < arr[middle]:
        high = middle
        return binary_search_recursive(arr, target, low, high)
    elif target > arr[middle]:
        low = middle
        return binary_search_recursive(arr, target, low, high)
    else:
        return False


print(binary_search_recursive.__doc__)
arr1 = [1,2,3,4,5,6,7,8,9,10]
print(binary_search_recursive(arr1, 4, 0, len(arr1) - 1))
print(binary_search_recursive(arr1, 9, 0, len(arr1) - 1))
print(binary_search_recursive(arr1, -12, 0, len(arr1) - 1))