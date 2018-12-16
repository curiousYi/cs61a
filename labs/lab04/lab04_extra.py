from lab04 import *

# Q13
def flatten(lst):
    """Returns a flattened version of lst.

    >>> flatten([1, 2, 3])     # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    """
    arr = []
    for i in range(0, len(lst)):
        if( type(lst[i]) == list):
            arr = arr + flatten(lst[i])
        else:
            arr.append(lst[i])
    return arr
# Q14
def merge(lst1, lst2):
    """Merges two sorted lists.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    firstListIndex = 0
    secondListIndex = 0
    arr = []

    while firstListIndex < len(lst1) and secondListIndex < len(lst2):
        if(lst1[firstListIndex] < lst2[secondListIndex]):
            arr.append(lst1[firstListIndex])
            firstListIndex = firstListIndex + 1
        else:
            arr.append(lst2[secondListIndex])
            secondListIndex = secondListIndex + 1
    
    if(firstListIndex >= len(lst1)):
        return arr + lst2[secondListIndex:len(lst2)]
    else:
        return arr + lst1[firstListIndex:len(lst1)]

