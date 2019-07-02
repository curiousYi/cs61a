import math
#######
# OOP #
#######

class Account:
    """An account has a balance and a holder.

    >>> a = Account('John')
    >>> a.deposit(10)
    10
    >>> a.balance
    10
    >>> a.interest
    0.02

    >>> a.time_to_retire(10.25) # 10 -> 10.2 -> 10.404
    2
    >>> a.balance               # balance should not change
    10
    >>> a.time_to_retire(11)    # 10 -> 10.2 -> ... -> 11.040808032
    5
    >>> a.time_to_retire(100)
    117
    """

    interest = 0.02  # A class attribute

    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        """Add amount to balance."""
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Subtract amount from balance if funds are available."""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance

    def time_to_retire(self, amount):
        """Return the number of years until balance would grow to amount."""
        assert self.balance > 0 and amount > 0 and self.interest > 0
        return math.ceil(math.log(amount/self.balance)/math.log(1+self.interest))

class FreeChecking(Account):
    """A bank account that charges for withdrawals, but the first two are free!

    >>> ch = FreeChecking('Jack')
    >>> ch.balance = 20
    >>> ch.withdraw(100)  # First one's free
    'Insufficient funds'
    >>> ch.withdraw(3)    # And the second
    17
    >>> ch.balance
    17
    >>> ch.withdraw(3)    # Ok, two free withdrawals is enough
    13
    >>> ch.withdraw(3)
    9
    >>> ch2 = FreeChecking('John')
    >>> ch2.balance = 10
    >>> ch2.withdraw(3) # No fee
    7
    >>> ch.withdraw(3)  # ch still charges a fee
    5
    >>> ch.withdraw(5)  # Not enough to cover fee + withdraw
    'Insufficient funds'
    """
    withdraw_fee = 1  # A class attribute
    free_withdrawals = 2

    def __init__(self, account_holder):
      Account.__init__(self, account_holder)
      self.free_withdrawals = FreeChecking.free_withdrawals

    def withdraw(self, amount):
      amount_to_withdraw = amount

      if self.free_withdrawals != 0:
        self.free_withdrawals -= 1
      else:
        amount_to_withdraw += FreeChecking.withdraw_fee

      return Account.withdraw(self, amount_to_withdraw)

###########
# Mobiles #
###########

# Tree definition

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def mobile(left, right):
    """Construct a mobile from a left side and a right side."""
    return tree(None, [left, right])

def sides(m):
    """Select the sides of a mobile."""
    return branches(m)

def side(length, mobile_or_weight):
    """Construct a side: a length of rod with a mobile or weight at the end."""
    return tree(length, [mobile_or_weight])

def length(s):
    """Select the length of a side."""
    return label(s)

def end(s):
    """Select the mobile or weight hanging at the end of a side."""
    return branches(s)[0]

def weight(size):
    """Construct a weight of some size."""
    assert size > 0
    return tree(size); 

def size(w):
    """Select the size of a weight."""
    assert is_leaf(w)
    return label(w)

def is_weight(w):
    """Whether w is a weight, not a mobile."""
    return is_leaf(w)

def examples():
    t = mobile(side(1, weight(2)),
               side(2, weight(1)))
    u = mobile(side(5, weight(1)),
               side(1, mobile(side(2, weight(3)),
                              side(3, weight(2)))))
    v = mobile(side(4, t), side(2, u))
    return (t, u, v)


def total_weight(m):
    """Return the total weight of m, a weight or mobile.

    >>> t, u, v = examples()
    >>> total_weight(t)
    3
    >>> total_weight(u)
    6
    >>> total_weight(v)
    9
    """
    if is_weight(m):
        return size(m)
    else:
        return sum([total_weight(end(s)) for s in sides(m)])

def balanced(m):
    """Return whether m is balanced.
    >>> t, u, v = examples()
    >>> balanced(t)
    True
    >>> balanced(v)
    True
    >>> w = mobile(side(3, t), side(2, u))
    >>> balanced(w)
    False
    >>> balanced(mobile(side(1, v), side(1, w)))
    False
    >>> balanced(mobile(side(1, w), side(1, v)))
    False
    """
    if(is_weight(m)):
      return True

    left_side = sides(m)[0]
    right_side = sides(m)[1]
    left_weight_or_mobile = end(left_side)
    right_weight_or_mobile = end(right_side)
    
    """
      See if the torques are equal
    """
    left_torque = length(left_side) * total_weight(left_weight_or_mobile)
    right_torque = length(right_side) * total_weight(right_weight_or_mobile)
    
    if left_torque != right_torque:
      return False

    """
      verify that the sub_mobiles are balanced
    """
    if not is_weight(left_weight_or_mobile) and not balanced(left_weight_or_mobile):
      return False
    
    if not is_weight(right_weight_or_mobile) and not balanced(right_weight_or_mobile):
      return False

    return True

def with_totals(m):
    """Return a mobile with total weights stored as the label of each mobile.

    >>> t, _, v = examples()
    >>> label(with_totals(t))
    3
    >>> print(label(t))                           # t should not change
    None
    >>> label(with_totals(v))
    9
    >>> [label(end(s)) for s in sides(with_totals(v))]
    [3, 6]
    >>> [label(end(s)) for s in sides(v)]         # v should not change
    [None, None]
    """
    m_total_weight = total_weight(m)
    left_side = sides(m)[0]
    right_side = sides(m)[1]
    left_side_length = length(left_side)
    right_side_length = length(right_side)
    left_side_mobile = end(left_side)
    right_side_mobile = end(right_side)

    if(is_weight(left_side_mobile)):
      m_left_weight = left_side_mobile
    else:
      m_left_weight = with_totals(left_side_mobile)

    if(is_weight(right_side_mobile)):
      m_right_weight = right_side_mobile
    else:
      m_right_weight = with_totals(right_side_mobile)
    
    m_left_side = side(length(left_side), m_left_weight)
    m_right_side = side(length(right_side), m_right_weight)

    return tree(m_total_weight, [m_left_side, m_right_side])

############
# Mutation #
############

def make_counter():
    """Return a counter function.

    >>> c = make_counter()
    >>> c('a')
    1
    >>> c('a')
    2
    >>> c('b')
    1
    >>> c('a')
    3
    >>> c2 = make_counter()
    >>> c2('b')
    1
    >>> c2('b')
    2
    >>> c('b') + c2('b')
    5
    """
    def counterContainer():
      cache = {}
      
      def counter(string):
        if string not in cache:
          cache[string] = 1
        else:
          cache[string] += 1
        return cache[string]
      
      return counter

    return counterContainer()

def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    """
    fib  = [0,1]
    counter = 0

    def get_next_fib():
      nonlocal fib, counter
      length = len(fib)

      if(counter > length - 1):
        fib.append(fib[length-1] + fib[length-2])

      number_to_return = fib[counter]
      counter = counter + 1
      
      return number_to_return

    return get_next_fib

def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> w(90, 'hax0r')
    'Insufficient funds'
    >>> w(25, 'hwat')
    'Incorrect password'
    >>> w(25, 'hax0r')
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    """
    password = password
    attempts = []
    balance = balance

    def withdraw(withdrawal, pw_attempt):
      nonlocal password, attempts, balance

      if len(attempts) == 3:
        return "Your account is locked. Attempts: {}".format(attempts)
      elif pw_attempt != password:
        attempts.append(pw_attempt)
        return "Incorrect password"
      else:
        if(balance < withdrawal):
          return "Insufficient funds"
        balance = balance - withdrawal
        return balance

    return withdraw

def make_joint(withdraw, old_password, new_password):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    auth_attempt = withdraw(0, old_password)

    if(type(auth_attempt) == str):
      return auth_attempt
    else:
      def wrapper_withdraw(withdrawal, pw_attempt):
        if(pw_attempt == new_password):
          return withdraw(withdrawal, old_password)

        return withdraw(withdrawal, pw_attempt)

      return wrapper_withdraw
