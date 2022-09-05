# Uzdevums 3
# import string  # normally i would import directly
# alphabet = string.ascii_lowercase
# print(alphabet)

def is_pangram(text, alphabet="abcdefghijklmnopqrstuvwxyz"):
    # torf = set(text).issuperset(set(alphabet))
    # result = set(text) >= set(alphabet)  #same as above line
    # print(torf)
    # return result
    return set(text.lower()) >= set(alphabet)  # of course we could do set(alphabet) <= set(text)

print(is_pangram("The five boxing wizards jump quickly"))

a_lv = 'aābcčdeēfgģhiījkķlļmnņoprsštuūvzž'
print(is_pangram('Tfū, čeh, džungļos blīkšķ, zvaņģim jācērp!', alphabet=a_lv))

print(is_pangram("defg", "abc"))
print(is_pangram("abbbac", "abc"))
set("abadd").
