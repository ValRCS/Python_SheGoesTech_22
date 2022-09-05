def get_common_elements(seq1, seq2, seq3):
    # return tuple(set(seq1).intersection(set(seq2).intersection(set(seq3))))
    # return tuple(set(seq1).intersection(set(seq2), set(seq3)))
    return tuple(set(seq1) & set(seq2) & set(seq3))  # same as above


print(get_common_elements("abcd", ['a', 'b', 'd'], ('b', 'c', 'd')))


# Ex. 2b
def get_common_elements_b(*sequences):
    if len(sequences) == 0:
        return ()
    return tuple(set(sequences[0]).intersection(*sequences[1:]))  # * unpacks the list


print(get_common_elements_b("abcd", ['a', 'b', 'd'], ('b', 'c', 'd')))
print(get_common_elements_b("abcd", ['a', 'b', 'd'], ('b', 'c', 'd'), "defgh", "dēlis"))
print(get_common_elements_b("abcd", ['a', 'b', 'd'], ('b', 'c', 'd'), "defgh", "dēlis", "Rīga"))

# difference between * and nothing
print(*[1, 2, 3], sep=" ")
print([1,2,3])

