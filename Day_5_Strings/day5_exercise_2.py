# 2. Almost Hangman

# Write a program to recognize a text symbol

# The user (first player) enters the text.

# Only asterisks instead of letters are output.

# Assume that there are no numbers, but there may be spaces.

# The user (i.e. the other player) enters the symbol.

# If the letter is found, then the letter is displayed in ALL the appropriate places, all other letters remain asterisks.

# Example:

# First input: Kartupeļu lauks -> ********* *****

# Second input: a -> *a****** *a***




# In principle, this is a good start to the game of hangman.

# https://en.wikipedia.org/wiki/Hangman_(game)
# text = input("Enter your set word: ")
# set_word = ""
# guess_word = ""

# for c in text:
#     if c == ' ':
#         set_word += " "
#     else:   
#         set_word += "_"
# print(set_word)

# guess = input("Enter your guess: ")

# for c in text:
#     if c == guess:
#         guess_word += c
#     elif c == ' ':
#         guess_word += " "
#     else:
#         guess_word += "_"
# print(guess_word)

# text = input('Please enter a text ').lower()
# display_list = []
# text_length = len(text)
# star = '*'

# for i in text:
#     display_list += star
#     # print(display_list)

# end_of_game = False

# while not end_of_game:
#     guess = input("Please guess a letter!: ").lower()
#     # clear()

#     if guess in display_list:
#         print(f"You have already guessed {guess}!")

#     for position in range(text_length):
#         letter = text[position]

#         if letter == guess:
#             display_list[position] = letter    

#     print(display_list)

#     if star not in display_list:
#         end_of_game = True
#         print("You win!")


text=input("First player, please enter a text")

space = " "
asterisk="*"
new_text=""

for c in text:
    if c == space:
        new_text += space  
    else: 
        new_text += asterisk 

print(new_text)

while asterisk in new_text:
    letter=input("Second player, please enter a letter")
   # letter="a"
    for i, c in enumerate(text): # so enumarate returns index and value
        if c == letter:
           new_text=new_text[:i]+letter+new_text[i+1:]
    print(new_text)

#NOT WORKING
print("GAME OVER")
print(new_text)

# TODO add game counter
# TODO add game limits