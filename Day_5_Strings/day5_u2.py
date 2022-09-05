word = input("First player, enter the text: ")
# word = "Kartupeļu lauks"

#guessed = "".join("*" for char in word) # downside is that this will include the empty space
guessed = "*"*len(word) # same as above
letter = " "  # to add back the spaces before starting
#
while not letter == "0":
    # for i in range(len(word)):
    for i, c in enumerate(word): # more Pythonic
        # if word[i].lower() in letter.lower():  # guesses are not case sensitive
        if c.lower() in letter.lower():  # guesses are not case sensitive
            guessed = guessed[:i] + word[i] + guessed[i + 1:]

    if guessed.find("*") == -1:
        print("Good job!")
        break

    print(guessed)
    letter = input("Player 2: Guess a letter (or input 0 to give up): ")

print(f"The word is: {word}")

# a way to do just the exercise (without full game loop)
#
# guess_text = ""
# for c in word:
#     if c == " ":
#         guess_text += " "
#     else:
#         guess_text += "*"
#
# print(guess_text)
#
# guess = input("Input a letter to guess")
#
# guess_text = ""  # to make a full game we would want to preserve the guess so far
#
# for c in word:
#     if c == " ":
#         guess_text += " "
#     elif c == guess:
#         guess_text += c
#     else:
#         guess_text += "*"
#
# print(guess_text)
