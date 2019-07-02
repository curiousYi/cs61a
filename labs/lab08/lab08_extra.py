class Keyboard:
    """A Keyboard takes in an arbitrary amount of buttons, and has a
    dictionary of positions as keys, and values as Buttons.

    >>> b1 = Button(0, "H")
    >>> b2 = Button(1, "I")
    >>> k = Keyboard(b1, b2)
    >>> k.buttons[0].key
    'H'
    >>> k.press(1)
    'I'
    >>> k.typing([0, 1])
    'HI'
    >>> k.typing([1, 0])
    'IH'
    >>> b1.pressed
    2
    >>> b2.pressed
    3
    """

    def __init__(self, *args):
      self.buttons= {}
      for key in args:
        self.buttons[key.pos] = key

    def press(self, info):
        """Takes in a position of the button pressed, and
        returns that button's output"""
        typed_key = self.buttons[info]
        typed_key.pressed += 1
        return typed_key.key

    def typing(self, typing_input):
        """Takes in a list of positions of buttons pressed, and
        returns the total output"""
        output = ""
        for key_press in typing_input:
          output += self.press(key_press)
        return output

class Button:
    def __init__(self, pos, key):
        self.pos = pos
        self.key = key
        self.pressed = 0

def make_advanced_counter_maker():
    """Makes a function that makes counters that understands the
    messages "count", "global-count", "reset", and "global-reset".
    See the examples below:

    >>> make_counter = make_advanced_counter_maker()
    >>> tom_counter = make_counter()
    >>> tom_counter('count')
    1
    >>> tom_counter('count')
    2
    >>> tom_counter('global-count')
    1
    >>> jon_counter = make_counter()
    >>> jon_counter('global-count')
    2
    >>> jon_counter('count')
    1
    >>> jon_counter('reset')
    >>> jon_counter('count')
    1
    >>> tom_counter('count')
    3
    >>> jon_counter('global-count')
    3
    >>> jon_counter('global-reset')
    >>> tom_counter('global-count')
    1
    """
    global_counter = 0

    def make_counter():
      nonlocal global_counter
      count = 0
      
      def counter(command):
        nonlocal count
        nonlocal global_counter
        if command == 'global-count':
          global_counter +=1
          return global_counter

        if command == 'global-reset':
          global_counter = 0

        if command == 'count':
          count += 1
          return count
        
        if command == 'reset':
          count = 0
      return counter

    return make_counter

def trade(first, second):
    """Exchange the smallest prefixes of first and second that have equal sum.

    >>> a = [1, 1, 3, 2, 1, 1, 4]
    >>> b = [4, 3, 2, 7]
    >>> trade(a, b) # Trades 1+1+3+2=7 for 4+3=7
    'Deal!'
    >>> a
    [4, 3, 1, 1, 4]
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c = [3, 3, 2, 4, 1]
    >>> trade(b, c)
    'No deal!'
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c
    [3, 3, 2, 4, 1]
    >>> trade(a, c)
    'Deal!'
    >>> a
    [3, 3, 2, 1, 4]
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c
    [4, 3, 1, 4, 1]
    """
    m, n = 1, 1
    found = False
    while(m < len(first) and n < len(second) and found == False):
      if(sum(first[:m]) == sum(second[:n])):
        found = True
      elif(sum(first[:m]) > sum(second[:n])):
        n += 1
      else:
        m += 1

    if m < len(first) and n < len(second): # change this line!
        first[:m], second[:n] = second[:n], first[:m]
        return 'Deal!'
    else:
        return 'No deal!'

def zap(n):
    i, count = 1, 0
    while i <= n:
        while i <= 5 * n:
            count += i
            print(i / 6)
            i *= 3
    return count
