# we will use unittest module to test our functions
# documentation for unittest is here
# https://docs.python.org/3/library/unittest.html
# first we import unittest module
import unittest
import my_fun
import my_class

# then we make a class that inherits from unittest.TestCase
class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(my_fun.add(0, 2), 2)
        self.assertEqual(my_fun.add(2, 2), 4)
        self.assertEqual(my_fun.add(-2, 2), 0)
        self.assertGreater(my_fun.add(2, 3), 4)
        # so we have many different assert methods here

# lets make a class to test our MyList class
class TestMyList(unittest.TestCase):
    # we need a special setUp method to create our instance of MyList
    def setUp(self): # it will run before each test 
        self.my_list = my_class.MyList()
        self.my_list.add(2)
        self.my_list.add(3)
        self.my_list.add(5)
        # we can also use self.addCleanup() to clean up after ourselves
        # this is not necessary here but could be useful in other cases

    def test_get_list(self):
        self.assertEqual(self.my_list.get_list(), [2, 3, 5])

    def test_get_sum(self):
        self.assertEqual(self.my_list.get_sum(), 10)

    def test_get_average(self):
        self.assertEqual(self.my_list.get_average(), 3.3333333333333335) # funny floats
        # so for floats we can use assertAlmostEqual which takes a delta
        self.assertAlmostEqual(self.my_list.get_average(), 3.3333333333333335, places=3) # better

# then we run the tests
if __name__ == '__main__':
    unittest.main()


# now if your function refers to global variables it will be much harder to test
# so you should try to avoid global variables, strive to make your functions pure - meaning some input and some output
# and no side effects - for print we do not have a choice but for other functions we should try to avoid side effects