# 3. Text conversion

# Write a program for text conversion

# Save user input

# Print the entered text without changes

# Exception: if the words in the input are not .... bad, 
# then the output is not ...  bad section must be changed to is good



# Examples:

# The weather is not bad -> The weather is good

# The car is not new -> The car is not new

# This cottage cheese is not so bad -> This cottage cheese is good 

# Hints:

# Find (or index, or even rfind) will probably come in handy, as may an operator. Also slice syntax will be useful.

# Extra: How would you do this task in Latvian language (nav slikts/a -> ir labs/a)?

text = input("Enter Your text, tell me about today's weather?")
print(text) #Weather is very bad
term_1 = "not"
term_2 = "bad"

find_1 = text.find(term_1)
find_2 = text.find(term_2)
replace = "good"

if 0 < find_1 < find_2:
    text = text.replace(text[find_1:(find_2 + len(term_2))], replace)
elif 0 < find_2:
    text = text.replace(text[find_2:find_2 + len(term_2)], replace)
print(text)