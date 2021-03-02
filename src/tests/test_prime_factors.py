import prime_factors as p

def test_factorize_one():
    assert p.prime_factors(1) == []

def test_factorize_two():
    assert p.prime_factors(2) == [2]

def test_factorize_three():
    assert p.prime_factors(3) == [3]

def test_factorize_four():
    assert p.prime_factors(4) == [2, 2]

def test_factorize_six():
    assert p.prime_factors(6) == [2, 3]

def test_factorize_big_number():
    assert p.prime_factors(3 * 3 * 5) == [3,3,5]

# def test_is_two_prime():
#     assert p.is_prime(2) == True

# def test_is_three_prime():
#     assert p.is_prime(3) == True

# def test_is_four_prime():
#     assert p.is_prime(4) == False

# def test_is_five_prime():
#     assert p.is_prime(5) == True