user_input = input("Input two words separated by space to create key value pairs, or enter nothing to quit")
empty_dict = {}
while user_input != "":
    words = user_input.split(" ")
    if len(words) >= 2:
        empty_dict[words[0]] = words[1]
    else:
        print("not enough words to create an entry")
    user_input = input("Input two words separated by space to create key value pairs, or enter nothing to quit")

print(empty_dict)