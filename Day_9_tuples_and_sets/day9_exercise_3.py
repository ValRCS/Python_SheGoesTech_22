# 3. Is there a pangram?

# Write a function is_pangram(text, alphabet='abcdefghijklmnopqrstuvwxyz')

# that returns True when the text parameter contains all the letters passed in an alphabet.
# We return False otherwise



# pangram - sentence, word string containing all letters of the alphabet - https://en.wikipedia.org/wiki/Pangram

# We ignore spaces and believe that uppercase is as valid as lowercase, i. here A and a -> a




# print(is_pangram("The five boxing wizards jump quickly")) -> True
# print(is_pangram("Not a pangram")) -> False

# Bonus: test it also on Latvian alphabet:
# a_lv = 'aābcčdeēfgģhiījkķlļmnņoprsštuūvzž'

# print(is_pangram('Tfū, čeh, džungļos blīkšķ, zvaņģim jācērp!', alphabet=a_lv)) -> True

# Bonus: test it also on Lithuanian alphabet:
# a_lt = 'aąbcčdeęėfghiįyjklmnoprsštuųūvzž' # see if this correct

# some languages have perfect pangrams, some do not
# perfect pangram - a pangram that uses every letter of the alphabet at just once