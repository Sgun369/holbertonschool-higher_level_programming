#!/usrr/bin/python3
"""
a module that contains a function
that returns the sum of two integers a and b
"""
def add_integer(a, b=98):
    """ 
    a function that adds 2 integers
    a and b
    """
    if not (isinstance(a, (int, float))):
        raise TypeError("a must be an integer ")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        a = int(a) if isinstance(a, float) else a
        b = int(b) if isinstance(b, float) else b

        return a + b
