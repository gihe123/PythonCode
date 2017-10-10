import pytest
from primes import is_prime
@pytest.mark.parametrize("inputs,excepted",[(0,True),(1,False),(5,True),(4,False)])
def test_all(inputs,excepted):
	assert is_prime(inputs)==excepted