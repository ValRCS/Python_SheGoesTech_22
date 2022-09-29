# write a function of 3 arguments all strings
# function should return lexigraphically ordered string of unique characters
# these unique characters must be present in BOTH  of the first two strings 
# BUT not in the third "badstring"

# example:
# "abcf", "fab", "boo"  returns -> "af" 
# because "a" is in both "abc" and "fab" but not in "boo"
# same goes for "f" it is present in both "good strings" but not in "badstring"
# notice "b" is not in the result because it is in the badstring.

# slightly harder way would be to use loops and if statements to check each character
# the easy way is to use sets and set operations 😊

# either approach is acceptable

# def lexi(*arg):
#     if len(arg) != 3:
#         return 0 # same as someone, don't know how to output a message only
#     set1 = set(arg[0])
#     set2 = set(arg[1])
#     set3 = set(arg[2])
#     set_common = set1 & set2
#     # return "".join(sorted(set_common - (set_common & set3))) # common btwn 1 and 2 minus common with 3
#     return "".join(sorted(set_common - set3)) # common btwn 1 and 2 minus common with 3

def good_bad_strings(good_one,good_two,bad_one):

    sorted_list = sorted(set(good_one)&set(good_two)-set(bad_one))
    result = ''.join(sorted_list)
    return result

print(good_bad_strings("bolabcfc", "faolb", "bcf"))
print(good_bad_strings("abcf", "fab", "boo"))


def fun_3_arg(txt1, txt2, txt3):
    ad_tup1 = set(txt1)
    ad_tup2 = set(txt2)
    ad_tup3 = set(txt3)
    my_set = ad_tup1.intersection(ad_tup2)
    my_set.difference_update(ad_tup3)  # IN PLACE on my_set
    my_list = list(my_set)
    my_list.sort()
    print(my_list)
    return "".join( my_list)


print(fun_3_arg(txt1="abcf", txt2="fab", txt3="boo"))
print(fun_3_arg(txt1="abcfdkln", txt2="fabdhuriek", txt3="boofert"))

# print(lexi("abcf", "fab", "boo"))

 ## 1.One-liner with list

def ordered_string(seq1, seq2, seq3):    
    # good approach for smaller sequences
    # because checking for i in seq2 will be a bit slower
    # only problem we keep duplicates
    return "".join(sorted([i for i in seq1 if i in seq2 and i not in seq3]))
    
print(ordered_string("abcf", "fab", "boo"))
print(ordered_string("abcfdfadf", "fabdfa", "bodgvbo"))

# new_set = set("davdajdlafjdlajf")
# print(new_set) 
# new_set.some_randome_var = 55135
# print(new_set.some_randome_var)     