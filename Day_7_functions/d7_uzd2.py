# Exercise 2.

def is_palindrome(input_text: str) -> bool:
    input_text = input_text.replace(" ", "").lower()
    reversed_text = input_text[::-1]
    return input_text == reversed_text  # we already have the reversed text, so


print(is_palindrome("Alus ari ir   a sul a"))
print(is_palindrome("Nu nav palindroms"))
