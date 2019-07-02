def deep_len(lnk):
    """ Returns the deep length of a possibly deep linked list.
    >>> deep_len(Link(1, Link(2, Link(3))))
    3
    >>> deep_len(Link(Link(1, Link(2)), Link(3, Link(4))))
    4
    >>> levels = Link(Link(Link(1, Link(2)), \
            Link(3)), Link(Link(4), Link(5)))
    >>> print(levels)
    <<<1 2> 3> <4> 5>
    >>> deep_len(levels)
    5
    """
    if(isinstance(lnk.first, Link)):
      if(isinstance(lnk.rest, Link)):
        return deep_len(lnk.first) + deep_len(lnk.rest)
      else:
        return deep_len(lnk.first) + 1
    elif(isinstance(lnk.rest, Link)):
      return 1+deep_len(lnk.rest)
    else:
      return 1

def make_to_string(front, mid, back, empty_repr):
    """ Returns a function that turns linked lists to strings.

    >>> kevins_to_string = make_to_string("[", "|-]-->", "", "[]")
    >>> jerrys_to_string = make_to_string("(", " . ", ")", "()")
    >>> lst = Link(1, Link(2, Link(3, Link(4))))
    >>> kevins_to_string(lst)
    '[1|-]-->[2|-]-->[3|-]-->[4|-]-->[]'
    >>> kevins_to_string(Link.empty)
    '[]'
    >>> jerrys_to_string(lst)
    '(1 . (2 . (3 . (4 . ()))))'
    >>> jerrys_to_string(Link.empty)
    '()'
    """
    def to_string(linked_list):
      if linked_list == Link.empty:
        return empty_repr
      return front + str(linked_list.first) + mid + to_string(linked_list.rest) + back

    return to_string

def tree_map(fn, t):
    """Maps the function fn over the entries of t and returns the
    result in a new tree.

    >>> numbers = Tree(1,
    ...                [Tree(2,
    ...                      [Tree(3),
    ...                       Tree(4)]),
    ...                 Tree(5,
    ...                      [Tree(6,
    ...                            [Tree(7)]),
    ...                       Tree(8)])])
    >>> print(tree_map(lambda x: 2**x, numbers))
    2
      4
        8
        16
      32
        64
          128
        256
    """
    if(t.is_leaf()):
      return Tree(fn(t.label))
    else:
      mapped_branches = []
      for branch in t.brancGhes:
        mapped_branches.append(tree_map(fn,branch))
      return Tree(fn(t.label), mapped_branches)


def add_trees(t1, t2):
    """
    >>> numbers = Tree(1,
    ...                [Tree(2,
    ...                      [Tree(3),
    ...                       Tree(4)]),
    ...                 Tree(5,
    ...                      [Tree(6,
    ...                            [Tree(7)]),
    ...                       Tree(8)])])
    >>> print(add_trees(numbers, numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    >>> print(add_trees(Tree(2), Tree(3, [Tree(4), Tree(5)])))
    5
      4
      5
    >>> print(add_trees(Tree(2, [Tree(3)]), Tree(2, [Tree(3), Tree(4)])))
    4
      6
      4
    >>> print(add_trees(Tree(2, [Tree(3, [Tree(4), Tree(5)])]), \
    Tree(2, [Tree(3, [Tree(4)]), Tree(5)])))
    4
      6
        8
        5
      5
    """

   
    if(t1.is_leaf() and t2.is_leaf()):
      return Tree(t1.label+t2.label)
    elif(t1.is_leaf()):
      return Tree(t1.label+t2.label, [branch.copy_tree() for branch in t2.branches])
    elif(t2.is_leaf()):
      return Tree(t1.label+t2.label, [branch.copy_tree() for branch in t1.branches])
    elif(len(t1.branches) != len(t2.branches)):
      new_tree = Tree(t1.label+t2.label, [ add_trees(pair_branch_1, pair_branch_2) for pair_branch_1, pair_branch_2 in zip(t1.branches, t2.branches)])
      if(len(t1.branches) > len(t2.branches)):
        new_tree.branches = new_tree.branches + [branch.copy_tree() for branch in t1.branches[len(t2.branches):]]
      else: 
        new_tree.branches = new_tree.branches + [branch.copy_tree() for branch in t2.branches[len(t1.branches):]]
      return new_tree
    else:
      return Tree(t1.label+t2.label, [ add_trees(pair_branch_1, pair_branch_2) for pair_branch_1, pair_branch_2 in zip(t1.branches, t2.branches)])
    


# Link
class Link:
    """A linked list.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.first
    1
    >>> s.rest
    Link(2, Link(3))
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is Link.empty:
            return 'Link({})'.format(self.first)
        else:
            return 'Link({}, {})'.format(self.first, repr(self.rest))

    def __str__(self):
        """Returns a human-readable string representation of the Link

        >>> s = Link(1, Link(2, Link(3, Link(4))))
        >>> str(s)
        '<1 2 3 4>'
        >>> str(Link(1))
        '<1>'
        >>> str(Link.empty)  # empty tuple
        '()'
        """
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

# Tree
class Tree:
    def __init__(self, label, branches=[]):
        for c in branches:
            assert isinstance(c, Tree)
        self.label = label
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
        return 'Tree({0}{1})'.format(self.label, branches_str)

    def is_leaf(self):
        return not self.branches

    def __eq__(self, other):
        return type(other) is type(self) and self.label == other.label \
               and self.branches == other.branches
    
    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

    def copy_tree(self):
        return Tree(self.label, [b.copy_tree() for b in self.branches])
