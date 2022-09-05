# 3. Text conversion
#
# Write a program for text conversion
# Save user input
# Print the entered text without changes
#
# Exception: if the words in the input are not .... bad, then the output is not ...  bad section must be changed to
# is good
#
# Examples:
#
# The weather is not bad -> The weather is good
# The car is not new -> The car is not new
# This cottage cheese is not so bad -> This cottage cheese is good
#
# Hints:
# Find (or index, or even rfind) will probably come in handy, as may an operator. Also slice syntax will be useful.
#
# Extra: How would you do this task in Latvian language (nav slikts/a -> ir labs/a)?

#text = 'The weather is not so bad'


text = input("Input text ")

# we a looking for 2 words inside

left_term = "not"
right_term = "bad"

find_left = text.find(left_term)
find_right = text.find(right_term)
replace = "good"  # replace word

if 0 < find_left < find_right:     # both words exists and second one is after first
    text = text.replace(text[find_left:(find_right + len(right_term))], replace)

print(text)