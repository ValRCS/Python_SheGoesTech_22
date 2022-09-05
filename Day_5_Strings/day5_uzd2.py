# text = input("Enter a text:")
# hidden = "*" * len(text)  # TODO show spaces
# print(hidden)
# guess = input("Enter a symbol:")
# # i=1
# new_hidden = ""
# for s in text:
#     if s == guess:
#         new_hidden += s
#     else:
#         new_hidden += '*'
# print(new_hidden)


print("\n___________Exercise 2 ________________\n")

text = input("Input you word or phrase: ")
text_masked = ''
text_unmasked = ''
for c in text:
    if c == " ":
        text_masked += " "
    else:
        text_masked += "*"
print(text_masked)

# TODO put guessing in a while loop to have a game
guess_letter = input("Input your guess (one symbol): ")
for c in text:
    if c == guess_letter:
        text_unmasked += c
    elif c == " ":
        text_unmasked += " "
    else:
        text_unmasked += "*"
print(text_unmasked)