#  2. Christmas tree 

# Ask user to enter the height of the tree 

# Then Print the tree: Ex. height == 3 

# The printout would be: 

#   * 

#  *** 

# ***** 

# Note: remember that several symbols can be 
# printed at once, for example: print ("" * 10 + "*" * 6)

tree_height=int(input("Please enter height of the tree"))

print(tree_height)
stars=1

for i in range(1,tree_height+1):
    print(" " * (tree_height-i) +  "*" * stars)
    stars=stars+2
    # so improvement would be to calculate stars from i
    # stars = i*2-1

for i in range(1,tree_height+1):
    print(" " * (tree_height-i) +  "*" * (i*2-1))



