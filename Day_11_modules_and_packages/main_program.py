# # modular programming
# # advantages to modular programming
# # 1. code reusability - you can use the same code in multiple places, multiple applications
# # 2. code readability
# # 3. code maintainability - easier to fix bugs, less interdependencies
# # 4. code debuggability
# # 5. code testability
# # 6. code portability
# # 7. code scalability
# # 8. code security
# # 9. code performance
# # 10. code reliability
# # 11. code extensibility
# # 12. code flexibility
# # 13. code modularity
# # 14. code simplicity - focus on one thing at a time
# # 15. code efficiency
# # 16. code usability
# # 17. code consistency
# # 18. code elegance
# # 19. code robustness
# # 20. code scope - avoid name collisions
# # 21. code clarity

# # # import sys  # this is a module from Python standard library
# # # import os  # operating system
# # # # generally you want to import Python standard stuff first before moving onto our modules
# # import os
# import sys  # from standard library

# import my_mod  # my_mod is a module that I created, so my_mod.py must be in the same directory as this file

# # result = my_mod.add(3,8)  # this is a function from my_mod.py
# # print(result)
# # print(my_mod.PI, my_mod.txt, my_mod.mlist)
# # # so no conflict with txt or PI or mlist if we had them in this file

# # new_garage = my_mod.Garage("La biblioteca")  # create new object using class from my_mod.py
# # print(new_garage.gname)

# # # you can rename your module that you import
# # import my_mod as mm # so typically we can create a short two-three letter alias for our module
# # mm.add(5,100)
# # print(mm.PI, mm.txt, mm.mlist) # and so on
# # popular external modules and packages like to use short 2 or 3 letter aliases

# # from my_mod import add  # for those times when you are sure there are no name collisions
# # from my_mod import PI
# # print(add(5, 100))
# # print(PI) # so we can import specific functions or variables from a module
# # only danger is if you have a name collision with another module

# # from my_mod import add as my_add # custom name for those cases when you want a single import but have a name collision
# # # so now I can use this renamed function
# # my_add(2,7) # so this is the function called add in my_mod.py but I renamed it to my_add

# # # DO NOT USE THIS
# # # # from my_mod import * # THIS IS BAD PRACTICE !! leads to name collission and might not actually import everything

# # # this is a module that I created
# # import my_pkg.my_utils
# # # unfortunately I have to use the full path to the module
# # my_pkg.my_utils.util_add(3, 8) # so this is the function called util_add in my_utils.py

# # import my_pkg.subp.sub_utils # i imported sub_utils.py from subpackge folder from package folder
# # my_pkg.subp.sub_utils.sub_add(23, 8) # so this is the function called sub_add in sub_utils.py


# # import my_pkg.subp.sub_utils as su  # so import from subpackage a particular module with a different name
# # su.sub_add(100,300) # so su is the alias for sub_utils module

# # i could import a specific function from a module
# # from my_pkg.subp.sub_utils import sub_add
# # sub_add(200,300) # just beware name collisions
# # from my_pkg.subp.sub_utils import sub_add as add  # so import a specific function/calls/variable and alias it


# # #
# # #
# # # # from sub_map import prod_tools as u1_g2
# # #
# # # in Python main is just a name, it could be anything
# def main():  # main function name is not required, but it is a good practice for main entry point
#     print("running main_program.py residing at", __file__)

#     print("of course __name__ is main...", __name__)

#     print("I will start looking for modules in the following paths:")
#     print("sys.path is", sys.path)
#     print(my_mod.add(5, 10))
#     print(my_mod.mlist)
#     print(my_mod.txt)
# #     #
#     new_garage = my_mod.Garage("LNB")
#     print(new_garage.gname)

#     print("Python version", sys.version_info)
# #     print("Python will look for modules in order of:", "\n".join(sys.path))
# #     print("Current working directory is", os.getcwd())
# #     print("OS is ", os.name)
# #     #     # so how does Python search for modules

# #     # print(mm.add(1100,333))
# #     # print(mm.PI)
# #     # print(add(100,200))  #so I imported add function from my_mod module and called it here
# #     # print(PI)  # PI is just a variable in my_mod module, capitals are constants in Python by convention
# #     # print(my_add(10,50)) # so I imported add function from my_mod module as my_add and called it here
# #     # print(my_pkg.my_utils.util_add(50, 10))

# #     # my_pkg.subp.sub_utils.sub_add(30, 22)  #kind of long if you have to write it often
# #     # su.sub_add(30,20,2000)
# #     # print(su.MAGIC_PI)
# #     # sub_add(25, 20)
# #     # add(10, 2, 5)


# # #     # we put calls to other functions here
# # #     # initialize/config function(s)
# # #     # do stuff function(s)
# # #     # cleanup function(s)
# # #
# # #
# # # # if main_program was import main_program then the next part would no run
# # # # so-called main guard
# if __name__ == "__main__":
#     # you could have a setup or config function here
#     main()  # the main entry point
#     # we could do more stuff here
#     # for example we could have a cleanup function here
