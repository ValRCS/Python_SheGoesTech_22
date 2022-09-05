# 1. Confusion
#
# The user enters a name.
#
# You print user name in reverse (should begin with capital letter)
# then extra text: ",a thorough mess is it not ", then the first name of the user name then "?"
#
# Example:
#
# Enter: Valdis -> Output: Sidlav, a thorough mess is it not V?

name = input("Input your name: ")
# possibly check for length before proceeding
extra = ",a thorough mess is it not "
name_reversed = name[::-1]
print(f"{name_reversed.capitalize()}{extra}{name[:1].upper()}?")  # [:1] kind of rare approach to get first char
# but we will have no errors
print(name_reversed.title() + extra + name[0] + "?")
print(name_reversed.capitalize() + extra + name[0] + "?")
# alternative using f-string

