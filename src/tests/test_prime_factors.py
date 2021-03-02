import prime_factors as p

def test_prime_factor_one():
    assert p.prime_factors(1) == []

def test_prime_factor_two():
    assert p.prime_factors(2) == [2]

def test_prime_factor_three():
    assert p.prime_factors(3) == [3]

def test_prime_factor_four():
    assert p.prime_factors(4) == [2, 2]

def test_prime_factor_five():
    assert p.prime_factors(5) == [5]

def test_prime_factor_six():
    assert p.prime_factors(6) == [2, 3]

def test_three_factors():
    assert p.prime_factors(3 * 3 * 3) == [3, 3, 3]

def test_four_factors():
    assert p.prime_factors(2 * 3 * 5 * 31) == [2, 3, 5, 31]