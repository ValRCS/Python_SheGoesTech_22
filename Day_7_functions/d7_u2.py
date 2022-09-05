# 2. Palindrome
# Write the function is_palindrome (text)
# which returns a bool True or False depending on whether the word or sentence is read equally from both sides.
# PS You can start with a one-word solution from the beginning, but the full solution will ignore whitespace and uppercase and lowercase letters.
# is_palindrome ("Alus ari i ra    sula") -> True
# is_palindrome("ABa") -> True
# is_palindrome("nava") -> False
#
def is_palindrome(input_text):
    input_text = input_text.replace(" ", "").lower()
    reversed_text = input_text[::-1]
    return input_text == reversed_text # no need for if input_text == reversed_text:
    # return input_text == input_text[::-1]
    # one liner example, but we have to clean up twice
    # return input_text.replace(" ", "").lower() == input_text.replace(" ", "").lower()[::-1]

print(is_palindrome("Abbbbb a"))
print(is_palindrome("Alus ari   ira sula"))
print(is_palindrome(""))
print(is_palindrome("a roza upala na lapu azora"))
print(is_palindrome("not a palindrome"))

text = str(input("Enter your text please:\n"))
output = "\nYour text is"
output += " a palindrome!" if is_palindrome(text) else " NOT a polindrome!"
# same as above one liner
# if is_palindrome(text):
#     output += " a polindrome!"
# else:
#     output += " NOT a polindrome!"

print(output + "\n")
