# Problem set 1: Variables
# Reference: https://realpython.com/python-variables/

# Declare variable with integer value
integer_var = ??

# Declare variable with string value
string_var = ??

# Declare variable with boolean value
boolean_var = ??

def check():
    # Check if integer_var is an integer
    assert isinstance(integer_var, int), "integer_var must be an integer"

    # Check if string_var is a string
    assert isinstance(string_var, str), "string_var must be a string"

    # Check if boolean_var is a boolean
    assert isinstance(boolean_var, bool), "boolean_var must be a boolean"

    print("Congratulations! You have completed problem set 1!")
    return True