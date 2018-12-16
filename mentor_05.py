def num_digits(n):
    stringified_number = str(n)

    if stringified_number[1:] == '':
        return 1
    else:
        return 1 + num_digits(int(stringified_number[1:]))


def is_sorted(n):
    stringified_number = n
    if(not isinstance(n, str)):
        stringified_number = str(n)

    if(len(stringified_number) == 1):
        return True

    first_num = stringified_number[0]
    second_num = stringified_number[1]

    if first_num < second_num:
        return False
    else:
        return is_sorted(stringified_number[1:])


def mario_number(level):
    stringified_level = level

    if(not isinstance(level, str)):
        stringified_level = str(level)

    if stringified_level[0] == '0' or stringified_level == '':
        return 0
    elif stringified_level == '1':
        return 1
    else:
        return mario_number(stringified_level[1:]) + mario_number(stringified_level[2:])


def make_change(n):
    if n <= 0:
        return 0
    elif n >= 1 and n < 3:
        return 1 + make_change(n-1)
    elif n >= 3:
        return 1 + min([make_change(n-3), make_change(n-4)])
    else:
        print('hit else')
