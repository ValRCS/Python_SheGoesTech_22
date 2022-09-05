# 1f -> write the function get_word_usage (srcpath, destpath)
# The function opens the file and finds the most frequently used words
# recommendation to use Counter module!
# assume that the words are separated by either whitespace or newline (the good old split will come in handy)
# the saved list of words and frequency should be saved in destpath in the following form:
# vards skaits
# un 3423
# es 3242
# PS to test, for srcpath use the file that is poetry only and has no punctuation and also the words are all in lowercase

from collections import Counter


def get_word_usage(srcpath, destpath):
    with open(srcpath, encoding="utf-8") as fin:
        text = fin.read()
        text = text.replace("\n", " ").lower()
        # you might want to replace all multip
        # le whitespaces with a single whitespace
        words = text.split()  # list of words
        # you might want to get word lemmas here from the text with library such as nltk, or Spacy
        word_counter = Counter(words)
    with open(destpath, "w", encoding="utf-8") as fout:
        fout.write("word\tcount\n")  # write the header
        for word, count in word_counter.most_common():  # unpacking the tuple in each iteration
            fout.write(f"{word}\t{count}\n")
            # possible improvement save the results in a string and then write to file in one line
    return word_counter


my_counter = get_word_usage("veidenbaums_clean_punkts.txt", "veidenbaums_word_usage.tsv")  # tab separated values
print(my_counter.most_common(30))
