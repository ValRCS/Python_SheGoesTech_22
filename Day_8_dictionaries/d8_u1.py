from collections import Counter

def get_char_count(s):
    result = {}
    for i in s:
        if i in result:
            result[i] += 1  # we add 1 to value held by already existing key
        else:
            result[i] = 1  # otherwise we create a new key:value pair and initialize value at 1
    return result


print(get_char_count('hubba bubba'))
print(get_char_count('hubba bubba abracadabra MAGIJA mana'))

print(get_char_count([1, 2, 3, 3, 3, 2, 2, 1, 2, 1, 1, 1, 1, 15, 6, 6]))
print(get_char_count(["tomato", "potato", "ice cream", "potato"]))

user_input = input("Enter some text to count")
count_dict = get_char_count(user_input)
print(f"Your text:{user_input} has the following character counts: {count_dict}")

count = Counter(user_input)
print(count)
print(count.most_common(10))  # if you leave off number you would get everything
