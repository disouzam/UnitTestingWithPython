import pytest


@pytest.fixture()
def setup():
    print("\nSetup method")


def test1(setup):
    print("\nExecuting test1!")
    assert True


def test2():
    print("\nExecuting test2!")
    assert True
