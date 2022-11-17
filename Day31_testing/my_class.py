# lets make a simple class that holds a list of numbers
# and has a method to add a number to the list
# and a method to return the list
# and a method to return the sum of the list
# and a method to return the average of the list

# lets define our class
class MyList:
    # we will use a list to hold our numbers
    def __init__(self):
        print("initializing MyList")
        self.numbers = []

    # we will use a method to add a number to our list
    def add(self, num):
        self.numbers.append(num)

    # we will use a method to return our list
    def get_list(self):
        return self.numbers

    # we will use a method to return the sum of our list
    def get_sum(self):
        return sum(self.numbers)

    # we will use a method to return the average of our list
    def get_average(self):
        return sum(self.numbers) / len(self.numbers)


# lets test our class this would be manual approach
# if __name__ == '__main__':
#     # lets create an instance of our class
#     my_list = MyList()
#     # lets add some numbers to our list
#     my_list.add(2)
#     my_list.add(3)
#     my_list.add(5)
#     # lets print our list
#     print(my_list.get_list())
#     # lets print the sum of our list
#     print(my_list.get_sum())
#     # lets print the average of our list
#     print(my_list.get_average())