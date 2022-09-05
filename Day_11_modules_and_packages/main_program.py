# import sys  # this is a module from Python standard library
# import os  # operating system
# # generally you want to import Python standard stuff first before moving onto our modules
import os
import sys  # from standard library

# import my_mod  # my_mod is a module that I created


#
# import my_mod as mm # so typically we can create a short two-three letter alias for our module
# from my_mod import add  # for those times when you are sure there are no name collisions
# from my_mod import PI
# from my_mod import add as my_add # custom name for those cases when you want a single import but have a name collision

# DO NOT USE THIS
# # from my_mod import * # THIS IS BAD PRACTICE !! leads to name collission and might not actually import everything

# this is a module that I created
# import my_pkg.my_utils
# import my_pkg.subp.sub_utils


import my_pkg.subp.sub_utils as su  # so import from subpackage a particular module with a different name
from my_pkg.subp.sub_utils import sub_add
# from my_pkg.subp.sub_utils import sub_add as add  # so import a specific function/calls/variable and alias it


#
#
# # from sub_map import prod_tools as u1_g2
#
#
def main():  # main function name is not required, but it is a good practice for main entry point
    print("running main_program.py residing at", __file__)

    print("of course __name__ is main...", __name__)

    print("I will start looking for modules in the following paths:")
    print("sys.path is", sys.path)
    # print(my_mod.add(5, 10))
    # print(my_mod.mlist)
    # print(my_mod.txt)
    #
    # new_garage = my_mod.Garage("LNB")
    # print(new_garage.gname)

    print("Python version", sys.version_info)
    print("Python will look for modules in order of:", "\n".join(sys.path))
    print("Current working directory is", os.getcwd())
    print("OS is ", os.name)
    #     # so how does Python search for modules

    # print(mm.add(1100,333))
    # print(mm.PI)
    # print(add(100,200))  #so I imported add function from my_mod module and called it here
    # print(PI)  # PI is just a variable in my_mod module, capitals are constants in Python by convention
    # print(my_add(10,50)) # so I imported add function from my_mod module as my_add and called it here
    # print(my_pkg.my_utils.util_add(50, 10))

    # my_pkg.subp.sub_utils.sub_add(30, 22)  #kind of long if you have to write it often
    # su.sub_add(30,20,2000)
    # print(su.MAGIC_PI)
    # sub_add(25, 20)
    # add(10, 2, 5)


#     # we put calls to other functions here
#     # initialize/config function(s)
#     # do stuff function(s)
#     # cleanup function(s)
#
#
# # if main_program was import main_program then the next part would no run
# # so-called main guard
if __name__ == "__main__":
    main()
    # we could do more stuff here
