# 2. Common Elements



# Write a function that returns a tuple with common elements in three sequences. Inputs can be list, tuple, string.

# get_common_elements(seq1, seq2, seq3)

# Example:

# get_common_elements("abc", ['a', 'b'], ('b', 'c')) -> ('b',) # we return a tuple with a single element 

# # remember that we can convert strings to set with set(mystring), and set to tuple with tuple(myset)

# 2. b For those with some experience 

# BONUS:  make a function that can handle an arbitrary number of input sequences
# so function which takes any number of sequences and returns a tuple with common elements
# get_common_elements(seq1, seq2, seq3, seq4, seq5, seq6, seq7) etc :), so just like print takes any number of values

def get_common_elements(seq1, seq2, seq3):
    set1 = set(seq1)
    set2 = set(seq2)
    set3 = set(seq3)
    return  tuple(set1 & set2 & set3)
    
    #       TEST

result = get_common_elements("abc", ['a', 'b'], ('b', 'c'))
result = get_common_elements("abcd", ['a', 'b', 'e', 'd'], "Valdis")
result = get_common_elements("abcd", ['a', 'b', 'e', 'd'], "Egle")
print(result)

def get_common_elements_unlimited(*seq):
    if len(seq) == 0:
        return tuple()  # empty tuple
    return tuple((set(seq[0]).intersection(*seq[1:]))) # we can unpack the list of sets with *seq[1:]

print(get_common_elements_unlimited("abc", ['a', 'b'], ('b', 'c')))
print(get_common_elements_unlimited("abc", ['a', 'b'], ('b','a', 'c'), "Valdis", "Visvaldis"))

def get_common_elements_2b(*args):
    if len(args) == 0:
        return tuple()  #early return pattern

    seq_set = set(args[0])  # so at least one argument is guaranteed
    for seq in args[1:]:
        seq_set = seq_set & set(seq) # so we add intersection one by one

    return tuple(seq_set)

print(get_common_elements_2b("abc", ['a', 'b'], ('b', 'c')))
print(get_common_elements_2b("abc", ['a', 'b'], ('b','a', 'c'), "Valdis", "Visvaldis"))