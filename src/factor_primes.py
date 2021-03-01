
def prime_factors(n):
    if n == 1:
        return []

    factor = n

    for i in range(2, n):
        if n % i == 0:
            factor = i

    if factor == n:
        return [factor]
    else:
        return prime_factors(n // factor) + [factor]
