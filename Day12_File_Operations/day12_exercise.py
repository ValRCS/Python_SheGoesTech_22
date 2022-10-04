# Exercise
# read text from  sherlock_holmes_adventures.txt

# 1a -> write the function file_line_len(fpath), which returns the number of lines in the file

# check file_line_len("sherlock_holmes_adventures.txt") -> 12305



# 1b -> write the function get_text_lines(fpath), which returns a list with only those lines that contain text.

# So we want to avoid/filter out those lines that contain whitespace

# PS preferably use encoding = "utf-8" when reading 



# 1c -> write the function save_lines(destpath, lines)

# This function will store all lines into destpath file 

# 1d -> call save_lines with destpath being "pure_sherlock.txt" and lines being the text lines we cleaned from 1b

# 1e -> write the function clean_punkts(srcpath, destpath)

# function will open the srcpath file, clear it from https://docs.python.org/3/library/string.html#string.punctuation

# then function will save the cleaned text into destpath
# clean_punkts("pure_sherlock.txt", "clean_sherlock.txt")


# 1f -> write the function get_word_usage(srcpath, destpath)

# The function opens the file and finds the most frequently used words

# recommendation to use Counter module!

# assume that the words are separated by either whitespace or newline (the good old split will come in handy)

# the saved list of words and frequency should be saved in destpath in the following form:

# word, count
# un, 3423
# es, 3242

# in effect you will be saving in standard csv format - https://docs.python.org/3/library/csv.html
# you can use csv module for this, but it is not necessary
import os
from pathlib import Path

#1A: function to find lenght of file 
def file_line_len(file_name):
    # first approach - using len() function
    # not the best approach, because it reads the whole file into memory
    # with open(file_name, 'r') as f:
    #     return len(f.readlines())
    # better to use a counter
    file_len = 0
    with open(file_name, encoding="UTF-8") as f:
        for _ in f:  # will work even on large files
            file_len += 1
    return file_len

# print(file_line_len("sherlock_holmes_adventures.txt"))
print(os.getcwd())

# print(file_line_len("Day12_File_Operations/sherlock_holmes_adventures.txt"))

list_of_text_files = [file for file in Path().rglob("*.txt") if file.is_file()]
print(list_of_text_files)

for file in list_of_text_files:
    print(file.absolute(), "length", file_line_len(file))

# Windows use both \ and / as path separators (but not mixed)
# Linux and Mac use only / as path separator
# so i use raw string to avoid escaping
absolute_path = r"C:\Users\val-wd\Github\Python_SheGoesTech_22\Day12_File_Operations\sherlock_holmes_adventures.txt"
print(absolute_path, "length", file_line_len(absolute_path))

def get_text_lines(fpath):
    with open(fpath,encoding='utf-8') as f:
        # filter out lines that contain only whitespace
        # whitespace is defined by string.whitespace
        # https://docs.python.org/3/library/string.html#string.whitespace
        # whitespace is \n, \t, \r, \v, \f, ' '
        lines = [line.strip() for line in f if line.strip()]
        # lines = [line for line in lines if len(line.strip()) > 0]
    return lines

text_lines = get_text_lines("sherlock_holmes_adventures.txt")
print(text_lines[:10])
print(len(text_lines))

# # 1c -> write the function save_lines(destpath, lines)

# This function will store all lines into destpath file 

# def save_lines(destpath, lines, encoding='utf-8'):
#     with open(destpath, mode='w', encoding=encoding) as fout:
#         fout.writelines(lines)  # write all lines from list

def save_lines(destpath, lines, sep='\n', encoding='utf-8'):
    with open(destpath, "w", encoding=encoding) as f:
        for line in lines:
            f.write(line + sep)

# let's add a new line at the end of each line
# 
save_lines("pure_sherlock_b.txt", text_lines)
# if we ant to add a new line at the end of each line
text_lines_with_newlines = [line + '\n' for line in text_lines]
# then we pass empty string as a separator
save_lines("pure_sherlock.txt", text_lines_with_newlines, sep="")

import string
def clean_punkts(srcpath, destpath):
    with open(srcpath, encoding="utf-8") as fin, open(destpath, mode="w", encoding="utf-8") as fout:
        for line in fin:
            for character in line:
                if character in string.punctuation: # you could skip this if and just use replace
                    line = line.replace(character, '')                    
            fout.write(line)

srcpath='pure_sherlock.txt'
destpath='clean_sherlock.txt'
clean_punkts(srcpath, destpath)