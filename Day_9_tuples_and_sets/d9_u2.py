# 2. Common Elements
# Write a function that returns a tuple with common elements in three sequences. Inputs can be list, tuple, string.
# get_common_elements (seq1, seq2, seq3)
# Example:
# get_common_elements ("abc", ['a', 'b'], ('b', 'c')) -> ('b',) # we return a tuple with a single element
# # remember that we can convert strings to set with set(mystring), and set to tuple with tuple(myset)

def get_common_elements(seq1, seq2, seq3):
    return tuple(set(seq1) & set(seq2) & set(seq3))


print(get_common_elements("abc", ['a', 'b'], ('b', 'c')))


def get_common_elements_2b(*seq_list):
    if len(seq_list) == 0:
        return tuple()  #early return pattern

    seq_set = set(seq_list[0])  # so at least one argument is guaranteed
    for seq in seq_list[1:]:
        seq_set = seq_set & set(seq)

    return tuple(seq_set)

print(get_common_elements_2b("abc", ['a', 'b'], ('b', 'c'), set("abbba""")))

print(get_common_elements_2b("bbadadc", "adfadebadaa"))
print(get_common_elements_2b("bbadadc"))
print(get_common_elements_2b())
print(get_common_elements_2b(range(10,20), range(15,22), [16,19], (16,17,18,19,20)))
