import inspect

# initializing function
def get_function_name():
    # get the frame object of the function
    frame = inspect.currentframe()
    return frame.f_code.co_name
# printing function name
print("The name of function is : " +get_function_name()) # test_function

#This code is contributed by Edula Vinay Kumar Reddy
# Source: https://www.geeksforgeeks.org/python-how-to-get-function-name/
