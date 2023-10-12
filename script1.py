import pytest

# Production code
def fizzBuzz(value):
    return str(value)

# Tests
def test_return1With1PassedIn():
    retVal = fizzBuzz(1)
    assert retVal == "1"

def test_returns2With2Passedod():
    retVal = fizzBuzz(2)
    assert retVal == "2"