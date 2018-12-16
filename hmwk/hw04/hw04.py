HW_SOURCE_FILE = 'hw04.py'

###############
#  Questions  #
###############

def intersection(st, ave):
    """Represent an intersection using the Cantor pairing function."""
    return (st+ave)*(st+ave+1)//2 + ave

def street(inter):
    return w(inter) - avenue(inter)

def avenue(inter):
    return inter - (w(inter) ** 2 + w(inter)) // 2

w = lambda z: int(((8*z+1)**0.5-1)/2)

def taxicab(a, b):
    """Return the taxicab distance between two intersections.

    >>> times_square = intersection(46, 7)
    >>> ess_a_bagel = intersection(51, 3)
    >>> taxicab(times_square, ess_a_bagel)
    9
    >>> taxicab(ess_a_bagel, times_square)
    9
    """
    return abs(street(a) - street(b)) + abs(avenue(a) - avenue(b))


def squares(s):
    """Returns a new list containing square roots of the elements of the
    original list that are perfect squares.

    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    return [
        int(
            i**(1/2)
        ) 
        for i in s 
        if (i ** (1/2)).is_integer()
    ]

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    if( n<=3 ):
        return n
    else:
        return g(n-1) + 2 * g(n - 2) + 3 * g(n-3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 3

    p1, p2, p3 = 3, 2, 1
    index = 4

    while(index <= n):
        current_sum = p1 + 2 * p2 + 3 * p3
        p1, p2, p3 = current_sum, p1, p2
        index += 1

    return current_sum



def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    def paddle(current_index, current_point, increment, target):
        if(target == 1):
            return 1
        elif(current_index == target):
            return current_point
        else:
            if (current_index) % 7 == 0 or str(current_index).find('7') != -1:
                return paddle(current_index + 1, current_point - increment, -increment, target)
            else:
                return paddle(current_index + 1, current_point + increment, increment, target)

    return paddle(1, 1, 1, n)

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    def find_highest(amount):
        highest_so_far = 1
        i = 1
        while(i <= amount):
            if(i <= amount):
                highest_so_far = i
            i*=2
        return highest_so_far
    
    highest_possible_change = find_highest(amount)

    def count(amount, highest_possible_change):
        if(highest_possible_change == 1):
            return 1
        elif amount == 0:
            return 1
        elif amount < 0 or highest_possible_change < 0:
            return 0
        else:
            return count(amount-highest_possible_change, highest_possible_change) + count(amount, highest_possible_change/2)
    return count(amount, highest_possible_change)

###################
# Extra Questions #
###################

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    
    return (lambda func: lambda n: func(func, n)) ( lambda func, n: 1 if n == 1 else mul(n, func(func,sub(n,1))))
