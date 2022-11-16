# make a simple add function
def add(a, b):
    return a + b


# main guard

# unit test for add function
def test_add():
    # test the add function
    assert add(0, 2) == 2
    assert add(2, 2) == 4
    # lets test negative numbers
    assert add(-2, 2) == 0
    assert add(2, 3) == 5
    assert add('space', 'ship') == 'spaceship'
    # test list addition
    assert add([1, 2], [3, 4]) == [1, 2, 3, 4]

# so in this way of unit testing you would write a function 
# for each function you want to test
# this way of working is possible and is better than nothing
# however it is not the best way to do it
# because you have to write a lot of extra code
# and you have to write a lot of extra tests
# we will see a better way to do this in the next video

if __name__ == '__main__':
    test_add()
    # assert will throw an error if the condition is not met