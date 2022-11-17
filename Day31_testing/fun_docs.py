# we will use docstrings to document our functions
# also we will use doctest to test our functions

# remember """ creates a docstring after the function

# lets create a function that adds two numbers
def add(a, b):
    """
    Description: This function adds two similar objects that support addition
    Parameters: a and b are two objects of same type that support addition
    >>> add(2, 3)
    5
    >>> add(100, 200)
    300
    >>> add(100, 2900)
    3000
    """
    # you could have your regular code and comments here
    return a + b

# we can use doctest to test output as well

# lets create a function that prints a string
def print_string(s):
    """
    Description: This function prints a string
    Parameters: s is a string
    >>> print_string('hello')
    hello
    >>> print_string('Valdis')
    world
    """
    print(s) # remember print does not return anything but we can still test it

# this leaves main guard for other code such as interactive testing
if __name__ == '__main__':
    import doctest
    doctest.testmod()

# there are methodolgies such as test driven development where you write failing tests first
# then make those test pass by writing the code