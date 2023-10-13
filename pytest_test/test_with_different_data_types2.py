from pytest import approx


def test_floatAssert():
    assert (0.1 + 0.2) == approx(0.3)
