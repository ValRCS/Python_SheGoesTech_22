def is_pangram(text, alphabet='abcdefghijklmnopqrstuvwxyz'):
    return set(alphabet) <= set(text.lower())


a_lv = 'aābcčdeēfgģhiījkķlļmnņoprsštuūvzž'
print(is_pangram('Tfū, čeh, džungļos blīkšķ, zvaņģim jācērp!', alphabet=a_lv))
print(is_pangram('Tfū, čeh, džungļos , zvaņģim jācērp!', alphabet=a_lv))
print(is_pangram("The five boxing wizards jump quickly"))
print(is_pangram("Not a pangram"))
