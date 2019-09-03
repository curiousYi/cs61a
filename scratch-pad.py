def gen_all_items(list_of_iterators):
    """
    >>> nums = [[1, 2], [3, 4], [[5, 6]]]
    >>> num_iters = [iter(l) for l in nums]
    >>> list(gen_all_items(num_iters))
    [1, 2, 3, 4, [5, 6]]
    """
    list = []
    for iterator in list_of_iterators:
        for thing in iterator:
            list.append(thing)
    return list