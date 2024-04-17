from Crypto.Util.number import *
from sympy import nextprime
from mewtool.number.util import *
from mewtool.rsa.wiener import wiener_find_d


def solve_a(n, e, c):
    """Decrypt message with prime factors of n by the nearest prime from the square root of n"""
    q = isqrt(n)
    while n % q != 0:
        q = nextprime(q)

    p = n // q
    tot = (p - 1) * (q - 1)

    d = pow(e, -1, tot)
    m = pow(c, d, n)

    return long_to_bytes(m)


def solve_b(n, e, c):
    """Decrypt message with n = p ** 2"""
    p = isqrt(n)
    tot = p * (p - 1)

    d = pow(e, -1, tot)
    m = pow(c, d, n)

    return long_to_bytes(m)


def solve_c(n, e, c):
    """Decrypt using the Wiener's attack"""
    d = wiener_find_d(e, n)

    if d is None:
        raise Exception(f"Wiener's attack failed")

    m = pow(c, d, n)

    return long_to_bytes(m)


def solve_d(n, e, c):
    """Decrypt when message is sort and e is small"""
    m = icbrt(c)
    return long_to_bytes(m)


def solve_e(n, e, c):
    """Decrypt when n is prime"""
    tot = n - 1
    d = pow(e, -1, tot)
    m = pow(c, d, n)

    return long_to_bytes(m)
