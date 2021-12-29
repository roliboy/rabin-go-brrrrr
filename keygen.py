from random import randint
from itertools import count


""" Checks whether a given number is prime or not
(7) -> true
"""
def is_prime(n):
    return all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))


""" Returns a random prime number in the specified range
(10, 20) -> 13
"""
def random_prime(start, end):
    return next(n for n in map(lambda x: randint(start, end), count()) if is_prime(n))


""" Generate a public and private key pair
(16) -> 9185248367, (105971, 86677)
"""
def generate_keys(magnitude):
    p = random_prime(2 ** magnitude, 2 ** (magnitude + 1))
    q = random_prime(2 ** magnitude, 2 ** (magnitude + 1))
    n = p * q
    return n, (p, q)
