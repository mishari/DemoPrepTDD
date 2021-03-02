
def prime_factors(n):
    if n == 1:
        return []

    if n % 2 == 0:
        return [2] + prime_factors(n // 2)

    for i in range(3, n, 2):
        if n % i == 0:
            return [i] + prime_factors(n // i)

    return [n] 
