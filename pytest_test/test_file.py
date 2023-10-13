# pylint: disable=line-too-long

"""This is a sample test module"""
class TestClass:
    """A docstring for a test class  - This docstring following conventions of https://peps.python.org/pep-0257/"""
    def test_me(self):
        """Test_me"""
        assert True

    def test_me2(self):
        """Test_me2"""
        assert True

class MyTestClass():
    """This class doesn't follow Python conventions to test classes - but docstring follows https://peps.python.org/pep-0257/"""

    def test_it(self):
        """Test_it"""
        assert True


    def test_it2(self):
        """Test_it2"""
        assert True
