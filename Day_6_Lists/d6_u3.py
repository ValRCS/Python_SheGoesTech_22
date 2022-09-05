sentence = input("Input the sentence: ")
words = sentence.split()
print(words)
# reversed_word_list = [word[::-1] for i, word in enumerate(words)]  # here we are not using i but it is nice to have if you want
reversed_word_list = [word[::-1] for word in words]  # here we are not using i but it is nice to have if you want
# reversed_word_list = [word[::-1] for word in words if len(word) > 2]  # with short word filter
print(reversed_word_list)
reversed_sentence = ' '.join(reversed_word_list).capitalize()
print(f"{sentence} -> {reversed_sentence}")