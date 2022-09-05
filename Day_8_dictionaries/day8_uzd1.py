# Ex. 1
from collections import Counter


def get_char_count_1a(text):
    char_count_dict = {}
    for i in text:
        if i in char_count_dict:
            char_count_dict[i] += 1
        else:
            char_count_dict[i] = 1
    return char_count_dict


hubba_dict = get_char_count_1a("hubba hubba")

print(hubba_dict)
print(get_char_count_1a("Mary had a little lamb"))
print(get_char_count_1a("Mary had a little lamb".lower()))


def get_char_count_1b(text):
    count = Counter(text)
    return count  # result will be sorted


print(get_char_count_1b("Mary had a little lamb"))  # Counter has some extra methods
print(dict(get_char_count_1b("Mary had a little lamb")))

print(get_char_count_1a(["Valdis", "alus", "Valdis", "alus", "piens", "alus"]))