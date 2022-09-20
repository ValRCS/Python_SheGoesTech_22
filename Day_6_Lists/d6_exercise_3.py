# 3. Reversed words

# The user enters a sentence.

# We output all the words of the sentence in a reverse form. 
# - not the whole text reversed!!

# Example

# Alus kauss mans -> Sula ssuak snam
# notice how each word was reversed separately

# PS Split and join operations could be useful here.

sentence = input('Enter a sentence, please: ')
words = sentence.lower().split()

# reversed_words=[]
# for word in words:
#     reversed_words.append(word[::-1])
# same as above
reversed_words = [word[::-1] for word in words]
# capitalize the first letter of first word
reversed_words[0] = reversed_words[0].capitalize()
# create a new string from the list
new_sentence = ' '.join(reversed_words)

#maybe I should check the uppercase...
print(new_sentence)