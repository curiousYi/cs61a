from lab03 import *

def is_palindrome(n):
    """
    Fill in the blanks '_____' to check if a number
    is a palindrome.

    >>> is_palindrome(12321)
    True
    >>> is_palindrome(42)
    False
    >>> is_palindrome(2015)
    False
    >>> is_palindrome(55)
    True
    """
    x, y = n, 0
    f = lambda: x % 10
    while x > 0:
        x, y = _____, f()
    return y == n

def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 2:
        return 2
    else:
        return n * skip_mul(n - 2)

def count_up(n):
    """Print out all numbers up to and including n in ascending order.

    >>> count_up(5)
    1
    2
    3
    4
    5
    """
    def counter(i):
        "*** YOUR CODE HERE ***"
    counter(1)

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    starter = n

    def is_divisible(number, divider):
        if(divider == number):
            return True
        elif(divider < number):
            if(number % divider == 0):
                return False
            else:
                return is_divisible(number, divider+1)

    return is_divisible(starter, 2)    

def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """
    index = 1
    sum = 0

    def next_summand( index, is_odd ):
        if is_odd:
            return odd_term(index)
        else:
            return even_term(index)

    def sum_up(current_index, is_odd):
        if current_index == n:
            return next_summand(current_index, is_odd)
        else:
            return next_summand(current_index, is_odd) + sum_up(current_index + 1, not is_odd)
    
    return sum_up(index, True)

def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    def get_first_digit(n):
        return int(str(n)[:1])
    
    def calculate_number_of_tens(n, target):
        if n < 10:
            if n == target:
                return 1
            else:
                return 0
        else:
            if get_first_digit(n) == target:
                return 1 + calculate_number_of_tens(int(str(n)[1:]), target)
            else:
                return calculate_number_of_tens(int(str(n)[1:]), target)


    def calculate_tens_for_first_digit(n):
        return calculate_number_of_tens(int(str(n)[1:]), 10-get_first_digit(n))

    def calculate_tens(n):
        if n >= 10 and n < 100:
            return calculate_tens_for_first_digit(n)
        else:
            return calculate_tens_for_first_digit(n) + calculate_tens(int(str(n)[1:]))
    
    return calculate_tens(n)
    



