def prime_factors(n):
    if n == 1:
        return []
    elif n % 2 == 0:
        return [2] + prime_factors(n // 2) 
    else:
        for i in range(3, n):
            if n % i  == 0:
                return i
        return [n]
