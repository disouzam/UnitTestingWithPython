import pytest

# Production code
def fizzBuzz(value):
    return str(value)

# Tests
def checkFizzBuzz(value, expectRetVal):
    retVal = fizzBuzz(value)
    assert retVal == expectRetVal

def test_return1With1PassedIn():
    checkFizzBuzz(1, "1")

def test_returns2With2Passedod():
    checkFizzBuzz(2, "2")