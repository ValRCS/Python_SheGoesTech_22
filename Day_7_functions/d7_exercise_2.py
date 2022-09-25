# 2. Palindrome


# Write the function is_palindrome(text)

# which returns a bool True or False depending on whether the word or sentence is read equally from both sides.

# PS You can start with a one-word solution from the beginning, but the full solution will ignore whitespace and uppercase and lowercase letters.


# is_palindrome ("Alus ari i ra    sula") -> True

# is_palindrome("ABa") -> True

# is_palindrome("nava") -> False
# Python has type hints, which are not mandatory but can be used to help the developer
# type hints are like United Nations letters, they are not mandatory but they are useful

def is_palindrome(some_text: str) -> bool:
    format_text = some_text.lower().replace(" ", "")
    # if format_text==format_text[::-1]:
    #     result=True
    # else:
    #     result=False
    # return result
    # this is the same as above, but shorter
    return format_text == format_text[::-1]

# lower level approach


def Palindroms(txt):
    txt = txt.lower().replace(" ", "")
    left = 0
    right = len(txt) - 1
    while right >= left:
        if txt[left] != txt[right]:
            return False
        left += 1
        right -= 1
    return True

print(Palindroms('Santa'))
print(Palindroms('Alus ari i ra    sula'))

# my_text  = input("Input text: ")
my_text = "Alus ari i ra    sula"
print(is_palindrome(my_text))
tests = ["Alus ari i ra    sula", "ABa", "nava", ""]
for test in tests:
    print(is_palindrome(test))

# so these type hints are not for our program but for special program checking tools
# called linters - pylance, pyright and others

# for some reason this is not working in VS Code at the moment...
