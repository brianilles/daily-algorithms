def linear_search(arr, target):
    """
    An algorithm for finding an item in a list.

    Input: array, target
    Output: item or False
    Runtime complexity: O(n)
    """
    for i in arr:
        if i == target:
            return i

    return False
    
print(linear_search.__doc__)
print(linear_search([1,2,3,4,5,6,7], 3))
print(linear_search([11,12,3,14,5,6,7], 40))
print(linear_search([1,12,3,483,23,6,7], 483))
print(linear_search([31,2,34,4,5,6,7], 40))
print(linear_search([1,23,3,44,5,68,7], 86))