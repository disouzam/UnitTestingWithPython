import pytest

paramVariable = [1, 2, 3]


@pytest.fixture(params=paramVariable)
def setup(request):
    retVal = request.param
    print("\nSetup! retVale = {}".format(retVal))
    return retVal


def test1(setup):
    print("\nsetup = {}".format(setup))
    assert True
