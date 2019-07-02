def vending_machine(snacks):
    """Cycles through sequence of snacks.

    >>> vender = vending_machine(('chips', 'chocolate', 'popcorn'))
    >>> vender()
    'chips'
    >>> vender()
    'chocolate'
    >>> vender()
    'popcorn'
    >>> vender()
    'chips'
    >>> other = vending_machine(('brownie',))
    >>> other()
    'brownie'
    >>> vender()
    'chocolate'
    """
    next_item_loc = 0

    def vender():
      nonlocal next_item_loc 

      if(next_item_loc == len(snacks)):
        next_item_loc = 1
      else:
        next_item_loc = next_item_loc + 1

      return snacks[next_item_loc - 1]

    return vender

