import pytest

# Production code
def fizzBuzz(value):
    return "1"

# Tests
def test_return1With1PassedIn():
    retVal = fizzBuzz(1)
    assert retVal == "1"