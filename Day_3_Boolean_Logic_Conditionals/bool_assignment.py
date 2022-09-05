a = True or 55 or 777 or 'hello'
print(a)  #prints first true value
d = False or 2*2==5 or "Tieto" or -6
print(d)

# and works differently
b = True and 66
print(b) # prints last true value
c = True and 66 and 'Valdis'
print(c) # prints last true value
# https://docs.python.org/3/reference/expressions.html#and
# it's alittle language trick, should be used sparingly

# almost everything is truthy
# very few are falsey - https://docs.python.org/3/library/stdtypes.html