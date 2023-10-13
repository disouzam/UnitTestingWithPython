import inspect


def setup_function(function):
    function_name = function.__name__
    if function_name == "test1":
        print("\nSetting up test1!")
    if function_name == "test1":
        print("\nSetting up test2!")
    else:
        print("\nSetting up unknown test!")


def teardown_function(function):
    function_name = function.__name__
    if function_name == "test1":
        print("\nTearing down test1!")
    if function_name == "test1":
        print("\nTearing down test2!")
    else:
        print("\nTearing down unknown test!")


def test1():
    print("Executing " + (inspect.currentframe()).f_code.co_name + "!")
    assert True


def test2():
    print("Executing " + (inspect.currentframe()).f_code.co_name + "!")
    assert True
