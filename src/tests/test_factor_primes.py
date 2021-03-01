from factor_primes import *

def test_factorize_one():
    assert prime_factors(1) == []

def test_factorize_two():
    assert prime_factors(2) == [2]

def test_factorize_three():
    assert prime_factors(3) == [3]

def test_factorize_four():
    assert prime_factors(4) == [2, 2]

def test_factorize_six():
    assert prime_factors(6) == [2, 3]

def test_factorize_ten():
    assert prime_factors(10) == [2,5]
    