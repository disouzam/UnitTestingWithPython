import pytest


@pytest.fixture(autouse=True)
def setup():
    print("\nSetup method")


def test1():
    print("\nExecuting test1!")
    assert True


def test2():
    print("\nExecuting test2!")
    assert True
