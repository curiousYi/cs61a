## Generators

def make_generators_generator(g):
    """Generates all the "sub"-generators of the generator returned by
    the generator function g.

    >>> def ints_to(n):
    ...     for i in range(1, n + 1):
    ...          yield i
    ...
    >>> def ints_to_5():
    ...     for item in ints_to(5):
    ...         yield item
    ...
    >>> for gen in make_generators_generator(ints_to_5):
    ...     print("Next Generator:")
    ...     for item in gen:
    ...         print(item)
    ...
    Next Generator:
    1
    Next Generator:
    1
    2
    Next Generator:
    1
    2
    3
    Next Generator:
    1
    2
    3
    4
    Next Generator:
    1
    2
    3
    4
    5
    """
    generator = g()
    list_of_generators = []
    list_of_values = []

    #This will implicity call the next on the generator
    for i in generator:
        list_of_values.append(i)
        current_length = len(list_of_values)
        def next_generator():
            q = 0
            while q < current_length:
                yield list_of_values[q]
                q+=1
        list_of_generators.append(next_generator())
    return list_of_generators

def permutations(lst):
    """Generates all permutations of sequence LST. Each permutation is a
    list of the elements in LST in a different order.

    The order of the permutations does not matter.

    >>> sorted(permutations([1, 2, 3]))
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    >>> type(permutations([1, 2, 3]))
    <class 'generator'>
    >>> sorted(permutations((10, 20, 30)))
    [[10, 20, 30], [10, 30, 20], [20, 10, 30], [20, 30, 10], [30, 10, 20], [30, 20, 10]]
    >>> sorted(permutations("ab"))
    [['a', 'b'], ['b', 'a']]
    """
    if not lst:
        yield []
        return
    
    if len(lst) == 1:
        return lst
    elif len(lst) == 2:
        return [
            [lst[0], lst[1]] ,
            [lst[1], lst[0]] 
        ]
    else:
        output = []
        permuted_lists_of_lists = permutations(lst[1:])
        for permutation in permuted_lists_of_lists:
            for i in range(0, len(permutation)):
                new_permutation = permutation[0:i] + lst[0] + permutation[i]
                output.append(new_permutation)
        return output