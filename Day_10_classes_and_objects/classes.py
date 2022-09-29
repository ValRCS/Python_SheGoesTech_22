# # OOP - Object Oriented Programming
# # OOP is a programming paradigm that uses objects
# #  and their interactions to design and program applications.
# # Classes and Objects
# # # # # # # # # # # # # # Python Class
# # # # # # # # # # # # # # Classes -> combine related data(properties)
# # # # # # # # # # # # # # Classes -> combine related functionality(methods)
# # # # # # # # # # # # # # Classes: blueprints
# # # # # # # # # # # # # # Objects - instances of class

# # # # # # # # # # # # # # Objects: concrete realization of those blueprints
# # # # # # # # # # # # # # https://docs.python.org/3/tutorial/classes.html
# # # #
# # # # # # # # # # # # # # how to store and process data about garage
# # # # # # # # # # # my_garage = ["paint can", "old papers", "rotting potatoes"]
# # # # # # # # # # # my_garage_d = {"paints": ["white", "black"], "food": "potatoes"}
# # # # # then i want to write some functions on how to deal with this garage
# # # # # OOP lets us combine values/properties and functions/methods in a single entity
# # # #
# # # # # # # # # # # # # # empty class definition
# # # # # # # # # #
# # # #
# class EmptyClass:  # EmptyClass is just a name I made up, Classes start with Capital letter
#     pass  # pass is empty instruction


# # #
# # #
# # # #
# # # #
# # # # # # # # # # # # # # # # # # i create an  based on class blueprint
# # # #
# # empty_class_instance_object = EmptyClass()  # creating an object
# # print(type(empty_class_instance_object))
# # # # # # # # # # # # # # # not great OOP style but i can add to an existing object
# # empty_class_instance_object.paint = ["red", "blue"] # i can add arbitrary properties
# # empty_class_instance_object.papers = ["Diena"]
# # empty_class_instance_object.owner = "Valdis"
# # print(empty_class_instance_object.paint)
# # # # # # #
# # # # empty_class_instance_object.my_value = 55
# # # # print(empty_class_instance_object.my_value)
# # # # # so I can store data in an object
# # # # # but we are not utilizing blueprints/templates
# # # # # # # # # # # # # empty_class_instance_object
# # empty_2 = EmptyClass() # so different object based on same EmptyClass
# # empty_2.painter = "Picasso"
# # empty_2.paint = "Guasha"
# # print(empty_2.paint, empty_class_instance_object.paint)
# # #
# # # # # # # # # # # # # # the simplest empty class definition
# # # #
# # # # # # # # # # # # # color = "Global color"
# # # #
# # # #
# class House:
# #     #     # #     # class method example meaning method we can use without any objects created
# #     #     # #     # a library could be created by grouping class methods
# # so this is a class method which will be available to all objects created from this class
# #     #     # #     # we can use it without creating any objects
#     @classmethod
#     def add(cls, a, b):
#         print(a, b, a + b, cls.all_house_prop)
#         return a + b

# #     #     #
#     all_house_prop = "Brick"  # class property generally meant to be shared among instances

# #     #
# #     #     # # # # # #     # do not share lists, dictionaries other mutable structures in class properties
#     def print_house_prop(self):  # method definition which is function associated with objects
#         print(f"This house is built from {self.all_house_prop}")

# #     #
# #     #     #
# #     #     # # # #     # so __init__ has to be exact name for constructor to be called
# #     #     # # # #     # __init__ is so called double under - dunder method
# # so good practice to have sane default values
#     def __init__(self, color="green", nails=0, owner=""):  # constructor method called upon creation of object
#         #         # we add everything that we want done when we first create object from our class blueprints
#         self.color = color  # self.color is a property of the object
#         # self.color = None  # of course we could have stuck with self.color = color
#         # self.set_color(color)  # by calling built in method we can perform extra validation
#         self.nails = nails
#         self.owner = owner
#         print(f"Initialized class instance with {self.color=} {self.nails=} {self.all_house_prop=} {self.owner=}")

# #     # so called setter method
#     def set_color(self, new_color):  # so called setter method
#         # some verification on sane color here maybe
#         # idea is to control how we set the value
#         self.color = new_color
#         print(f"Changed color to {self.color}")
#         return self  # by returning self we can chain methods

# #     #
# #     #     #
# #     #     # # #     # regular methods, so method is a function declared in class definition
#     def build_house(self):
#         print(f"Building a house of {self.all_house_prop}")
#         print(f"Its color will be {self.color}")
#         return self

# #     #
#     def simple_print(self):
#         print(f"Oh {self.color=} {self.nails=}")
#         return self  # this lets us chain our methods


# # #
# # #

# # # class definition ends here


# # # # #
# # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # no houses yet, so this is class method
# print(House.add(5, 11))


# # # # #
# # # #
# # # #
# new_house = House()  # I create a new object instance from House class blueprint
# # print(new_house.all_house_prop)
# # new_house.print_house_prop()  # so we call method associated with this object, (self does not have to be specified!!)
# # # # print(new_house.all_house_prop)  # could access the property directly
# # # # # print("This particular house is built from", new_house.all_house_prop)
# # # # # print(type(new_house), type(5), type("Valdis"))
# # # # #
# # # # # #
# # another_house = House()  # so each time we creat a new object __init__ is called for that object
# # print(another_house.all_house_prop)
# # another_house.print_house_prop()
# # another_house.all_house_prop = "Straw"
# # another_house.print_house_prop()
# # new_house.print_house_prop()  # my original house is still from brick
# # # # # #
# # my_house = House(owner="Valdis") # creaing new object, in other class instance
# # print(my_house.color, my_house.nails)
# # print(my_house.all_house_prop)
# # my_house.build_house()
# # # # # # # # my_house.all_house_prop = "Clay" # not very OOP style to mutate
# # # # # # # # print(my_house.all_house_prop)
# # # # # # # # my_house.build_house() # i am calling a method, notice no self needed
# # summer_house = House(nails=500)  # another object instance of same House class
# # summer_house.build_house()
# # # # print(summer_house.nails)
# # red_house = House(color='red')  # so self is not mentioned
# # print("Color", red_house.color)
# # # # # # # # third_house.build_house()
# # # # # # # # my_house.set_color("Orange")
# # # # # # # # print("Type", my_house.all_house_prop)
# # # # # # # # my_house.build_house()
# # # # # # # # # # # # # # # # # # # # i've created an object my_house based on House class blueprints
# # # # # # # # # # # # # print(type(my_house))
# # # # # # # # my_house.simple_print() # calling object's method
# # # # # #
# # friends_house = House(color="blue", nails=1_000, owner="Edgars")  # so new object based on same template
# # print(friends_house.color)
# # friends_house.build_house().set_color("yellow").build_house().simple_print()
# # same as
# # friends_house.build_house()
# # friends_house.set_color("yellow")
# # friends_house.build_house()
# # friends_house.simple_print()
# # just in one line
# # # friends_house.simple_print().set_color("yellow").build_house()
# # # friends_house.set_color("Violet").simple_print()  # this works because simple_print return self
# # #
# # #
# # # # # # # class methods can return self if they have nothing useful to return
# # # #
# # # # # # # # # # my_house.simple_print()
# # # # # # # # # # my_house.set_color("red")
# # # # # # # # # # my_house.simple_print()
# # # #
# # # # # # # # # # # # # def inside class defines method (so function which is called by class or object)
# # # #
# # # #
class Garage:
# #     g_name = "just a garage"  # not needed better to use sparingly we can run in some weird effects

# #     @classmethod  # this means that this method is a class method can be called without any objects
# #     def add(cls, a, b):
# #         print(a, b, a + b, cls.all_house_prop)
# #         return a + b

# #     #
# #     #     # # # #     # classes constructor method called when we make a new object instance from this class
# #     #     # # # #     # dunder syntax __init__
    def __init__(self, color="green", nails=0, name="My garage", nail_color="metal", secret="gold"):
        self.color = color
        self.nails = nails
        self.name = name
        self._nail_color = nail_color  # convention of private do not touch properties
        self.__secret_stash = secret  # private property whose name is mangled to outside
        print(f"Initialized class instance with {self.color=} {self.nails=} {self.name=}")

# there are other dunder methods
# list of all dunder methods
# https://rszalski.github.io/magicmethods/
# official docs
# https://docs.python.org/3/reference/datamodel.html#special-method-names

# #     #
# #     #     #
# #     #     # # #     # will be useful when we want to print our object
    def __str__(self):  # this is responsible for string representation for print etc
        # so naturally for __str__ we return a string
        return f"Garage name: {self.name} color {self.color} nails: {self.nails} secret: {self.__secret_stash}"

# #     #
# #     #
    def __add__(self, other):  # + operator overloading in other languages
        # return self.nails + other.nails
        new_color = self.color + "_" + other.color  # TODO make your color mixer
        new_nails = self.nails + other.nails
        # so I return a new garage with a mix of properties from incoming garages
        return Garage(color=new_color, nails=new_nails)  # i create new instance  with new attributes

# #     #
# #     #     #
    def __eq__(self, other):  # so == will work
        # we come up some logic for object comparison
        return self.color == other.color and self.nails == other.nails  # not a full comparison

# #     #
# #     #     #
# #     #     # # # #     # i could just live with __str__ no need for simple_print anymore
    def simple_print(self):  # so this name i just made up myself
        print(f"Oh {self.name=} {self.color=} {self.nails=}")
        return self

# #     #
    def add_nails(self, new_nails=1):
        # here could be code for checking validity of new nails
        self.nails += new_nails
        return self

# #     #
# #     #     #
# #     #     # so i can control how secret is to be given out
    def get_secret(self):
        # here i could check if secret should be given out and how
        return self.__secret_stash

# #     #
# #     #     #
    # so called setter method - we control how secret is changed
    def set_secret(self, new_secret):
        # here we can check if new secret is valid to be set
        if len(new_secret) >= 6:
            print("Good secret, setting it")
            self.__secret_stash = new_secret
        else:
            print("Secret is too short, needs to be at least 6 characters long")
        return self  # for chaining

# #     #     #
    def set_nails(self, new_nail_count=0):
        self.nails = new_nail_count
        return self

# #     #
# #     #     # this method really has no place inside here, since it has nothing to do with garage..
# #     def silly_add(self, a, b):
# #         print("just a utility for adding", a, b, a + b)
# #         return a + b

# #     #
# #     #     #
# #     # # #     # OOP getters method
# #     def get_current_nails(self):
# #         # formatting, data sanitation, so on
# #         return self.nails


# # #
# # #
# # # # # # # # end of our class definition, that is end of our blueprint
# # # #
# # # #
simple_garage = Garage()
print(simple_garage)  # without __str__ definition not very useful
print(simple_garage.color)
print(simple_garage.name)
print(simple_garage._nail_color) # we can access this semi-private property
# single _ simply means this should not be messed with
# but I could if I really wanted to
# print(simple_garage.__secret_stash) # this name has been mangled/sort of hidden
# # # solution controlled access to private variables using methods
# so called getter or accessor methods
print(simple_garage.get_secret())
simple_garage.set_secret("12345") # too short
simple_garage.set_secret("123456") # number on my garage door
print(simple_garage.get_secret())
print(simple_garage) # this will not look too good, just a memory address
# # simple_garage.simple_print()
# # simple_garage.add_nails(15)
# # simple_garage.simple_print()
# # # # # # # print(simple_garage)
# # # # # # # # # print(simple_garage.__secret_stash) # so __property is renamed using name mangling
# # # # # # # # print(simple_garage.get_secret()) # using getter to obtain private information
# # # #
# # # # # # print(simple_garage.g_name)
# # # # # # simple_garage.g_name = "Mana garāža"
# # # # # # print(simple_garage.g_name)
# # # # # # # # # # # to avoid always initalize by hand constructors were created
# # # #
# # # # # # # # # # # # # create new objects based on class definition
homer_garage = Garage(color="yellow", nails=33)
flanders_garage = Garage(color="blue", nails=55, name="Property of Flanders")
print(homer_garage)  # this works because we wrote our own __str__ method
print(flanders_garage)
mutant_garage = homer_garage + flanders_garage  # we created our own __add__ method, gaining syntax sugar
# print(mutant_garage)
mut_garage = homer_garage.__add__(flanders_garage)  # same as above

print(mutant_garage)
print(mut_garage)
# in order to compare objects we need to define __eq__ method
print("Objects have same contents", mut_garage == mutant_garage)  # we defined our garage __eq__ should be True
# so same contents but different objects
print("Objects are same in memory", mut_garage is mutant_garage)  # two different objects by id, so False
# # #
# # # #
# # # #
# # # # # # # garage_obj_1 = Garage()
# # # # # # # garage_obj_2 = Garage()
# # # # # # # print("Objects have same contents based on our __eq__ method", garage_obj_1 == garage_obj_2) # to compare we'd need to define our __eq__ method
# # # # # # # print("Objects are actually same in memory?", garage_obj_1 is garage_obj_2) # main thing that garage object reside in diffent memory location
# # # # # # # # # # # # # two different objects from the same blueprint(class defintion)
# # # # # print(id(homer_garage), id(flanders_garage))
# # # # # # # # # # # print(homer_garage)
# # # # # # print(homer_garage._nail_color) # means for internal use but not private
# # # # # # # # so with return self i can chain the calls on the smae object
# # # #
# so as long as a method returns self we can chain them

mutant_garage.simple_print().add_nails(77).simple_print().set_nails(500).add_nails(10).simple_print()
# # homer_garage.add_nails(50).add_nails(170).simple_print()  # so return self lets me chain methods
# # # # # # # # # # # # print(homer_garage.__secret_stash) # so __variables get name mangled
# # # # # # # # # # # # print(homer_garage.g_name)
# # # # # # # # # # # # print(Garage.g_name)
# # # # # # # # # # # # # homer_garage.simple_print()
# # # # # # # # # # # # # flanders_garage.simple_print()
# # millhouse_garage = Garage(color="purple")
# # millhouse_garage.simple_print()

# # millhouse_garage.silly_add(1, 6)  # this would be better as a utility method not part of the garage class
# # # it would be better as part of class as a class method

# # # print(millhouse_garage)
# # # #
# # # # # # # # # # # # homer_garage.g_name = "Homer's garage"
# # # # # # # # # # # # homer_garage.simple_print()
# # # # # # # # # # # # print(Garage.g_name)
# # # # # # # # # # # # print(homer_garage)
# # # # # # # # # # # # super_garage = homer_garage + flanders_garage
# # # # # # # # # # # # print(super_garage)
# # simpsons_house = House(color="yellow")
# # print(simpsons_house.color)


# # # # # # # # # # # # # simpsons_house.simple_print()
# # # # # print(simpsons_house)
# # # # # print(str(simpsons_house)) # i wouldneed to create __str__ method for House as well
# # # # # # # # # # # # # print(homer_garage.nails)
# # # # # # # # # # # # # print(homer_garage.get_current_nails())
# # # # # # # # # # # # # print(homer_garage.nails)
# # # #
# # # # # # # # # # # # # millhouse_garage.nails
# # # # # # # # # # # # # millhouse_garage.add_nails(7)
# # # # # # # # # # # # # millhouse_garage.add_nails(17)
# # # # # # # # # # # # # millhouse_garage.simple_print()
# # # millhouse_garage.add_nails(10).add_nails(25).simple_print()
# # # millhouse_garage.add_nails(5).simple_print()
# # # millhouse_garage.set_nails(-50).add_nails(10).simple_print()
# # #
# # #
# # # #
# # # # # # # # # # # # # # # homer_garage.paints = ["white", "black"]
# # # # # # # # # # # # # # # homer_garage.foods = "eaten"
# # # # # # # # # # # # # # # print(homer_garage.paints)
# # # # # # # # # # # # # # # print(homer_garage.foods)
# # # #
# # # # # # # # # principle of inheritance
# # # # # # # # # # # # # # # FancyGarage will inherit everything from Garage
# # # #
# # # # # # # # # # # # # inheritance
class FancyGarage(Garage):  # so I say that this class blueprints use all methods and attributes from Garage class
    # #     # Class Attributes
    gtype = "Fancy"
    total_travel = 0

# #     # #
# #     # # # # # # #     # constructor method, called when we created object from this class
# #     # # # # # # # if i am not happy with parent constructor, notice the single tuple
# #     # # # # # # # we do not put lists as default values to avoid trouble
# if i do not specify __init__ method, it will use the one from parent class automatically
    def __init__(self, cars=("Buggati",), wines=("Rioja", "Temparillo"), color="Gold", name="Garage"):
        #         # I call my parent class constructor
        #         # Python 3.x+ we call our parent class constructor
        # since I specify my own constructor, I need to call parent constructor
        super().__init__(color, nails=2000, name=name)  # so this will call Garage constructor
        # if you did not call super() you would not have access to parent class attributes
        # self.color = color  # for color this would work, but we would have no nails!!
        self.cars = list(cars)  # converting to list since I want to mutate
        self.wines = list(wines)
        print("Fancy Garage Created")
        self.pretty_print()

# #     #
# #     # # # # # # #     # we have to give self argument for all methods inside classes
    def pretty_print(self):
        print(f"{self.gtype=}, {self.cars=}, {self.wines=}, {self.total_travel=}")
        return self

    # #
    def drive(self, distance):
        print(f"Driving {self.cars} a distance of {distance}")
        self.total_travel += distance
        return self  # Allows chaining of objects

    def get_longest_wine(self):
        wines_length = sorted(self.wines, key=len, reverse=True)
        return wines_length[0]


# # # #
new_fancy_garage = FancyGarage()  # so we are using FancyGarage blueprint to create a new object
print(new_fancy_garage)
print(new_fancy_garage.total_travel)  # this was not present in plain garage
print(new_fancy_garage.set_secret("silver").set_nails(55).simple_print().get_secret())
# # # print(new_fancy_garage.total_travel)  # something new from FancyGarage
# # #
burns_garage = FancyGarage(["Bentley"], ["Rioja", "Temparillo", "Riesling"], color="Gray", name="Mr. Burn's Garage")
crusty_garage = FancyGarage(cars=["Rolls"], wines=["Cabernet", "Cheap Wine"], color="Bright Red", name="Crusty's Garage")
# # # #
print(burns_garage)  # __str__ comes from Garage definition
burns_garage.pretty_print()
# # burns_garage.add_nails(10).drive(20).drive(30).pretty_print().simple_print()
# # burns_garage.add_nails(50).drive(70).pretty_print().simple_print().pretty_print()


# # # # # # print(burns_garage.get_longest_wine())
# # # #
# # # # kent_garage = FancyGarage(["Ferrari"], wines=["Cheap Wine"],color="aquamarine")
# # # # kent_garage.pretty_print()
# # # #
# # # # kent_garage.add(65,100)
# # # #
# # # # # # # # # # # # # # print(burns_garage.cars)
# # # # # # # # # # # # # # print(burns_garage.wines)
# # # # # # # # # # # # # # burns_garage.gtype = "Rich"
# # # # # # # # # # # # # # burns_garage.pretty_print()
# # # # # # # # # # # # # # crusty_garage.pretty_print()
# # # #
# # # #
# # # # # # # # # # # # # # # crusty_garage.drive(60)
# # # # # # # # # # # # # # # crusty_garage.drive(160)
# # # # # # # # # # # # # # # crusty_garage.drive(20)
# # # # # # # # # # # # # # # crusty_garage.pretty_print()
# # # # # # # # # # # # # # # print(burns_garage.get_longest_wine())
# # # # # # # # # # # # # # # print(crusty_garage.get_longest_wine())
burns_garage.drive(100).drive(150).drive(80).pretty_print()
crusty_garage.drive(10).drive(25).pretty_print()
# # # # # # # # # # # # # # wilma_garage = Garage("pink")
# # # # # # # # # # # # # # wilma_garage.simple_print()
# # # # # # # # # # # # # # burns_garage.simple_print()
# # # # # # # # # # # # # # brockman_garage = FancyGarage("Ferrari", "Chuck Wine")
# # # # # # # # # # # # # # comic_guy_garage = FancyGarage("Ferrari", "Chuck Wine", "Bright Red")
# # # # # # # # # # # # # # comic_guy_garage.simple_print()  # can use Garage method
# # # # # # # # # # # # # # comic_guy_garage.pretty_print()  # can use Fancy Garage method
# # # #
class SimpleGarage(Garage):
    # so __init__ from original Garage is used and everything else from Garage plus
    # plus we just add a new method
    def count_my_nails(self):
        return self.nails


# # # #
# SimpleGarage actually has everything from Garage plus count_my_nails method
maggies_garage = SimpleGarage()  # so we are using SimpleGarage blueprint to create a new object
maggies_garage.add_nails(33).simple_print()
print(maggies_garage.count_my_nails())
lisa_garage = SimpleGarage()
print(lisa_garage)


class Person:
    def __init__(self, name, age, hobbies):
        self.name = name
        self.age = age
        self.hobbies = hobbies

valdis = Person("Valdis", 49, ["Python", "Cycling", "Chess"])

print(valdis.age)
print(valdis.hobbies)
print(valdis.name)

# alternative would be to use a dictionary

# animal Class without __init__
class Animal:
    # legs = 4
    # tail = True
    # can_fly = False
    # nickname = "Fluffy"
    # eats_meat = True
    # i like using sane common default values whenever possible
    def __init__(self, legs=4, tail=True, can_fly=False, nickname="", eats_meat=True):
        self.legs = legs
        self.tail = tail
        self.can_fly = can_fly
        self.nickname = nickname
        self.eats_meat = eats_meat

    def make_noise(self):
        print(f"Animal Noise from {self.nickname}")

# print uses __str__ - the human readable representation of the object
    def __str__(self):
        return f"{self.nickname} is an animal with {self.legs} legs and {self.tail} tail"   

# __repr__ is the machine readable representation of the object used by list etc
    def __repr__(self):
        return f"Animal({self.legs}, {self.tail}, {self.can_fly}, {self.nickname}, {self.eats_meat})"

tom = Animal(legs=4, tail=True, can_fly=False, nickname="Tom", eats_meat=True) # so tom is an instance of Animal class
print(tom.legs)
print(tom.tail)
print("Can Fly?", tom.can_fly)
print("Eats meat?", tom.eats_meat)
tom.is_cat = True # you can add more attributes to the object later on
# not good practice to add attributes to the object after it has been created but you can do it

# the downside is if you need to have very different animals
# then you would have to have a lot of attributes
# and constructor would come in handy

# I could use a dictionary instead
jerry = {"legs": 4, "tail": True, "can_fly": False, "nickname": "Jerry", "eats_meat": True}
print(jerry["legs"])
print(jerry["tail"])
print(jerry["nickname"])

# what happens if we want to add methods to our class?
# theoretically we could add methods to dictionary but more complex


chipmunk = Animal(nickname="Alvin", eats_meat=False)
print(chipmunk.nickname)
print(f"Chipmunk {chipmunk.nickname} eats meat? {chipmunk.eats_meat}")

print(chipmunk)
print(tom)

# so i can produce 10 no name animals and store them in a list
animal_list = [Animal(nickname=f"Animal No. {i}") for i in range(1,11)]
print(animal_list)
print(animal_list[0])

class GPS:
    def __init__(self, location="Riga"):
        self.location = location

class Car:
    def __init__(self, make="Opel", model="Astra", year=2015, color="Silver", gps=GPS()):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.gps = gps  #my car has a gps object

my_car = Car(make="VW", model="Golf", year=2019, color="Black", gps=GPS(location="Berlin"))

print(my_car.gps.location)

# multiple inheritance is possible
# you can inherit from multiple classes
# but you should be careful with it
# it can get complicated

class Frankenstein(Animal, Car):
    # we have two __init__ methods so we need to call both
    def __init__(self, legs=4, tail=True, can_fly=False, nickname="", eats_meat=True, make="Opel", model="Astra", year=2015, color="Silver", gps=GPS()):
        # ihave to call both __init__ methods
        Animal.__init__(self, legs, tail, can_fly, nickname, eats_meat)
        Car.__init__(self, make, model, year, color, gps)


# so Frankenstein has all the attributes from Animal and Car
monster = Frankenstein(nickname="Frank", eats_meat=False, make="VW", model="Golf", year=2019, color="Black", gps=GPS(location="Berlin"))
print(monster.nickname)
print("Eats meat?", monster.eats_meat)
print(monster.make)
print(monster.gps.location)
monster.make_noise() # again self is automatically passed to the method

