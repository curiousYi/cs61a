from lab07 import *

# Q6
def cumulative_sum(t):
    """Mutates t where each node's root becomes the sum of all entries in the
    corresponding subtree rooted at t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative_sum(t)
    >>> t
    Tree(16, [Tree(8, [Tree(5)]), Tree(7)])
    """
    if t.is_leaf():
      return 
    else:
      sum_of_branches = 0
      for branch in t.branches:
        cumulative_sum(branch)
        sum_of_branches += branch.label
      t.label = t.label + sum_of_branches

# Q7
def reverse_other(t):
    """Reverse the entries of every other level of the tree using mutation.

    >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(4), Tree(3), Tree(2)])
    >>> t = Tree(1, [Tree(2, [Tree(5, [Tree(7), Tree(8)]), Tree(6)]), Tree(3)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(3, [Tree(5, [Tree(8), Tree(7)]), Tree(6)]), Tree(2)])
    """
    def reverse_now(t):
      for branch in t.branches:
        reverse_other(branch)
      return
    
    branches_length = len(t.branches)
    half_of_branches_length = int(branches_length / 2)

    for i in range(0,half_of_branches_length):
      t.branches[i].label, t.branches[branches_length-1-i].label = t.branches[branches_length-1-i].label, t.branches[i].label
    for branch in t.branches:
      reverse_now(branch)
    return
# Q8
def deep_map_mut(fn, link):
    """Mutates a deep link by replacing each item found with the
    result of calling fn on the item.  Does NOT create new Links (so
    no use of Link's constructor)

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> deep_map_mut(lambda x: x * x, link1)
    >>> print(link1)
    <9 <16> 25 36>
    """
    if isinstance(link.first, Link):
      deep_map_mut(fn, link.first)
    else:
      link.first = fn(link.first)
      
    if isinstance(link, Link) and link.rest != Link.empty:
      deep_map_mut(fn, link.rest)

# Q9
def has_cycle(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle(u)
    False
    """
    link.touched = True;
    while(link.rest != Link.empty):
      link = link.rest
      if(hasattr(link, 'touched')):
        return True
    return False;

def has_cycle_constant(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    """
    link.touched = True;
    while(link.rest != Link.empty):
      link = link.rest
      if(hasattr(link, 'touched')):
        return True
    return False;
