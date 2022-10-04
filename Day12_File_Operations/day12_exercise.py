# Exercise
# read text from  sherlock_holmes_adventures_1661-0.txt

# 1a -> write the function file_line_len(fpath), which returns the number of lines in the file

# check file_line_len ("veidenbaums.txt") -> should be 971 or 972



# 1b -> write the function get_poem_lines (fpath), which returns a list with only those lines that contain poetry.

# So we want to avoid/filter out those lines that contain whitespace and also those lines with poem titles.

# PS preferably use encoding = "utf-8" 



# 1c -> write the function save_lines (destpath, lines)

# This function will store all lines into destpath file 

# 1d -> call save_lines with destpath being "veid_poems.txt" and lines being the poem lines we cleaned from 1b

# 1e -> write the function clean_punkts (srcpath, destpath)

# function will open the srcpath file, clear it from https://docs.python.org/3/library/string.html#string.punctuation

# then function will save the cleaned text into destpath

# 1f -> write the function get_word_usage (srcpath, destpath)

# The function opens the file and finds the most frequently used words

# recommendation to use Counter module!

# assume that the words are separated by either whitespace or newline (the good old split will come in handy)

# the saved list of words and frequency should be saved in destpath in the following form:

# vards skaits

# un 3423

# es 3242