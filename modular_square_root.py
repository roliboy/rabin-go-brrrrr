def mod_sqrt(a, p):
    if legendre_symbol(a, p) != 1:
        return 0

    s, e = partition(p)
    n = get_negative_legendre_symbol(p)
    x = pow(a, int((s + 1) / 2), p)
    b = pow(a, int(s), p)
    g = pow(n, int(s), p)

    while True:
        t = b
        m = 0
        for m in range(e):
            if t == 1:
                break
            t = pow(t, 2, p)

        if m == 0:
            return x

        gs = pow(g, 2 ** (e - m - 1), p)
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        e = m

def partition(p):
    s = p - 1
    e = 0
    while s % 2 == 0:
        s /= 2
        e += 1
    return s, e

def get_negative_legendre_symbol(p):
    n = 2
    while legendre_symbol(n, p) != -1:
        n += 1
    return n

def legendre_symbol(a, p):
    symbol = pow(a, int((p - 1) / 2), p)
    return -1 if symbol == p - 1 else symbol
