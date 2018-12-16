def ab_plus_c(a, b, c):
    """Computes a * b + c.

    >>> ab_plus_c(2, 4, 3)  # 2 * 4 + 3
    11
    >>> ab_plus_c(0, 3, 2)  # 0 * 3 + 2
    2
    >>> ab_plus_c(3, 0, 2)  # 3 * 0 + 2
    2
    """
    
    if(b == 0 or a == 0):
      return c
    elif(b == 1):
      return a + c ;
    else:
      return a + ab_plus_c(a, b-1, c)

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.
    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    if(a > b):
      larger, smaller = a, b
    else:
      larger, smaller = b, a

    if larger % smaller == 0:
      return smaller
    else:
      return gcd(smaller, larger % smaller)


def hailstone(n, counter = 0):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print(n)
    if(n == 1):
      return counter + 1
    elif(n % 2 == 0):
      newNumber = int(n/2)
      return hailstone(newNumber, counter+1)
    else:
      newNumber = int( n * 3 + 1)
      return hailstone(newNumber, counter+1)
