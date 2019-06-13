def binary_search_iterative(arr, target):
    """
    An algorithm for finding an item in a sorted list.
    1. compare the item in the middle of the list to the target
    2. if true, found
    3. if false, not found
    4. check if greater than or less than
    4. if less than, remove right hand side and repeat from 1
    5. if greater than, remove left hand side and repeat

    Input: a list if numbers (arr), a target
    Output: an item's index if found, false if not found
    Runtime complexity: O(log(n))
    """
   
    low = 0
    high = len(arr) - 1
    mid = (low + high) // 2

    while len(arr) >= 1:
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            high = mid 
            mid = (low + high) // 2
        elif target > arr[mid]:
            low = mid
            mid = (low + high) // 2
    else:
        return false

print(binary_search_iterative.__doc__)
print(binary_search_iterative([1,2,3,4,5,6,7,8,9], 5))
print(binary_search_iterative([1,2,3,4,5,6,7,8,9], 2))
print(binary_search_iterative([1,2,3,4,5,6,7,8,9], 8))