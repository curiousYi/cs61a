def divisors_of_n(n):
    return [i for i in range(1, n) if n % i == 0]

def perfect_numbers(n):
    return [i for i in range(1, n) if sum(divisors_of_n(i)) == i]