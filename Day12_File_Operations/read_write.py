# # # # # # # # # # # Reading and writing files
# # # # # # # # # # # https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# # # # # # # # # # # https://realpython.com/read-write-files-python/
# # # # # # # # # # # file - set of continuous bytes for storing data - various formats
# # # # # # # # # # # libraries for many common formats (CSV, JSON, etc)
# # # # # # # # # # # plain text files - encodings and line endings could be different
# # # # # # # # # # # usually we have Unicode today (encoding using UTF-8)
# # # # # # # # # # # creating file object (file stream)
# # # # # # # # # # # closing file automatically with with contextcd
import os
from re import L  # system library
import string
from datetime import datetime as dt  # datetime has datetime submodule(klase)
from pathlib import Path  # this is newer for path manipulation

# #
# # #
print(os.getcwd())  # current working directory
# print(os.listdir())  # an older way of getting file directory
# print(os.listdir(os.getcwd()))  # exactly the same as above
# files = Path(".").glob("*")  # this is newer way of getting file directory
# # . stands for current directory
# # .. stands for parent directory - one level up
# # # glob() - returns a list of paths that match the specified pattern
# # # # above is a generator object so it needs to be converted to list
# files = list(files)
# print(files)
# only_files = [f for f in files if f.is_file()]  # makes sure we only get files not folders
# only_dirs = [f for f in files if f.is_dir()]  # makes sure we only get folders not files
# print("My Files")
# print(only_files)
# print("My Folders")
# print(only_dirs)
# # # # difference is that Path will handle OS specific path separators
# text_files = [f for f in files if f.suffix == ".txt"]  # if i already have all files in list
# print(text_files)
# text_files_also = [f for f in Path(".").glob("*.txt") if f.is_file()]  # this is newer way of getting file directory
# print(text_files_also)
# # # "." is current directory
# # # "*.txt" is a wildcard for all text files
# # #
# # # I can use rglob to recursively get all files in a directory and subdirectories
# all_text_files_in_current_dir_and_subfolders = [f for f in Path(".").rglob("**/*.txt") if f.is_file()]
# print(all_text_files_in_current_dir_and_subfolders)
# all_text_files_in_parent_dir = [f for f in Path("..").rglob("*.txt") if f.is_file()]
# # ".." is parent directory
# # "**/*.txt" is a wildcard for all text files in child directories
# # "*.txt"
# print(all_text_files_in_parent_dir)

# # # # # # # # # # # # # with - context manager
# # #
# abs_path = os.path.abspath("frost.txt")
# print(abs_path)  # everybody will have their own unique absolute path
# # # # # # # # # using absolute path and manual file closing.. two things we usually want to avoid
# fstream = open(abs_path)  # r is not required it is the default
# # # # fstream is a file stream object, it is not the content of the file
# # # # i have opened a file and i want to read it
# # text = fstream.read() # read into string
# # fstream.close() # very important to close the file
# # print(text[:100])  # printing first 100 characters
# # # #
# # # #
# # # # # # # # # # # # we use with to guarantee closing of files
# # # # # # # # ## Absolute path will be different for pretty much everyone (different user name for one)
# generaly we want to avoid using absolute paths because they are different for everyone
# so i used r to indicate that it is a raw string - no escape characters
# otherwise i would have to use double backslash \\ to escape the backslash
# absolute_path = r"C:\Users\val-wd\Github\Python_SheGoesTech_22\Day12_File_Operations\frost.txt"
# fstream = open(absolute_path)
# text = fstream.read()
# fstream.close() # crucial that we close the file when not using a context manager
# print(text[:100])

# # #
# # # # Relative path example
# fstream = open("frost.txt")  # so this is relative to current working directory
# text = fstream.read()
# fstream.close() # often we forget to close the file
# print(text[:100])

# fstream = open("Day12_File_Operations/frost.txt")  # so this is relative to current working directory
# text = fstream.read()
# fstream.close()
# print(text[:100])
# # #
# # # a recommended approach is to use a context manager
# fstream could be called anything, f, file, fin, etc
# with open("frost.txt") as fstream:  # reading mode is implied, instead of fstream we can use f or anything else
#     text = fstream.read()
#     # fstream is still open
#     print("file stream is still open")
# # # fstream is already closed
# print(text)
# #
# #
# # # # # # # # # Relative Paths
# # # # # # # # # # if current directory is one level above our desired
# # # # # with open('Diena_12_Faili/frost.txt') as f:  # create a file object, default is read mode
# # # # #     print(f.read())
# # # # # # # # # # important! f is closed here already!!! it's a good thing
# # # # # os.chdir("Diena_12_Faili") # so we change our working directory to one level deeper
# # # # # # # # # one way of getting to current path is simply change in terminal where we start
# with open('frost.txt') as f:  # create a file object, default is read mode
#     print(f.read())  # so keep in mind this might not be best for HUUGe files
#     print("File is still open here")
#     print("Trying again")
#     print("Should have ----- new poem below -----")
#     print(f.read())  # no error but where is the content ?
# # #     print("Lets try again")
#     f.seek(0)  # put the needle of the record to beginning
#     print(f.read(20)) # so read 20 symbols from current needle position
#     print(f.seek(15))  # return the needle position
#     print(f.read(5))  # so this is the method you can use for fine reading
# # # # # # # # #     print(f.seek(50)) # so jumpe the needle to 50 from 0
# # # # # # # # #     print(f.read(15)) # so read from 51 to 65
# # # # # # # # #     # f is still open here
# # # # # # # # #     f.seek(0)
# # # # # # # # #     res = f.read()  # not very efficient use of course , might have read it all in beggining
# # # # # # # # # # # # # # # # # # # # # # f will be closed here already
# # # # # # # # # # # print(f.read()) # this will be error
# # # # # # # # # # # # # # # # # # # # # without with I would have to call f.close()
# # # # # # # # # print(res)
# # #
# # # # # # one level up just add more ../ for more levels
# # # with open("../LICENSE") as f:  # .. means one level up relative to our current working directory
# # #     print(f.read())
# # #
# # # # # # my_files = os.listdir("./") # current dir
# # # # # # print(my_files)
# # # # # # # print(os.listdir("C:/"))
# # #
# # # # one_level_up = os.listdir("../.")
# # # # print(one_level_up)
# # #
# # # # # # more modern is Path - better compatibility across OSes Windows/Mac/Linux
# # # # # # so going through current directory recursively getting all objects ending with .txt and making sure they are files
# # text_files = [f for f in Path("./").rglob("*.txt") if f.is_file()]  # rglob is recursive goes through subfolders
# # print(text_files)
# # # # # # # # from one level up recursively all text files in my project (one level up)
# # text_files = [f for f in Path("../.").rglob("*.txt") if f.is_file()]
# # print(text_files)
# # python_files = [f for f in Path("../.").rglob("*.py") if f.is_file()]
# # # print(python_files)  # a list of all python files in one level up
# # # # # # # from one level up just all text files in that level just glob
# # # # # text_files = [f for f in Path("../.").glob("*.txt") if f.is_file()]
# # # # # print(text_files)
# # # # current_text_files  = [f for f in Path("./").glob("*.txt") if f.is_file()]
# # # # # print(current_text_files)
# my_path = Path("frost.txt")  # so this will create correct name on all 3 OSes
# print(my_path)
# #
# with open(my_path) as f:
#     txt = f.read()
# # # # file is closed here
# # f is not open here
# print(txt)
# # # # # # # # # # # # # # # # list of supported encodings
# # # # # # # # # # # # # # # # https://docs.python.org/3/library/codecs.html#standard-encodings
# # # # # # # # # # # with open('Diena_12_Faili/frost.txt', encoding="utf-8") as f:  # create a file object
# with open('frost.txt', encoding="utf-8") as f:  # create a file object
#     res = f.read()  # it is quite possible that for large files we do not want it all at once
# print(res)
# # # # # # # # # # print(res[-30:])
# # # # # # # # # # # # so we can load War and Peace in memory but maybe a huge log file which could be 1TB will not fit
# # #
with open("frost.txt") as f:
    text = f.read()
print("File is closed already no access to f")
print(text)

# we want to add encoding="utf-8" to open function to make sure we can read all characters in all languages
with open("frost.txt", encoding="utf-8") as f:
    text = f.read()
print(text) # now we can read it

# list of other encodings
# https://docs.python.org/3/library/codecs.html#standard-encodings

with open("frost.txt", encoding="utf-8") as fstream:
    lines = fstream.readlines()  # reads all lines defined with newline
print(lines)  # this is a list
# # # # # # notice how \n is present
# it is present because we read it as is
# often we will want to write a file with \n anyways
# # #
# # # # # # # # # # # # # so with open('file.txt') as f: # we are opening file in read mode
# # #
# # # # # # # # # # with open('Diena_12_Faili/frost.txt', encoding="utf-8") as f:  # create a file object
# with open('frost.txt', encoding="utf-8") as f:  # create a file object
#     for line in f:  # so this will work even on huge files as long as each line ends with \n
#         print(line)  # of course for big files we will not want to print
#         print(line, end="")  # of course for big files we will not want to print
#         print(line.rstrip())  # get rid of all whitespace on right side
#         print(line.rstrip("\n"))  # most precise strips newline on right side
# # # # # # # # #         # quick and dirty and generally okay possible last line has no \n
#         print(line[:-1]) # possibly cut last char from last line
# # #
lines_without_newline = [line.rstrip("\n") for line in lines]
print(lines_without_newline)

# for writing we use open with mode="w" or mode="a" for append
# mode="w" will overwrite the file !!!
with open("frost_first_4_lines.txt", mode='w', encoding="utf-8") as fout:
    fout.writelines(lines[:4])  # write all lines from list

# append to file
with open("frost_first_4_lines.txt", mode='a', encoding="utf-8") as fout:
    fout.writelines(lines[4:8])  # write all lines from list
    fout.write("This is a new line\n")  # write a new line to the file



# # # # # # # # # with open('frost.txt', encoding="utf-8") as f:  # create a file object
# # # # # # with open('frost.txt', encoding="utf-8") as f:  # create a file object
# # # # # #     mylines = f.readlines()  # could also read a few lines with f.readline()
# # #
# # # # # # print(mylines[:5])  # print first five lines
# # #
# # # # # # # # # # with open('Diena_12_Faili/frost.txt', encoding="utf-8") as f:  # create a file object
# # # # # # # # # #     # could also read a few lines with f.readline()
# # # # # # # # # #     mylines = [line[:-1] for line in f]
# # # # # # # # # #     # 99.9%  of time newline ends with /n
# # #
# # # # # # # # # # print(mylines[:5])
# # #
# with open('frost.txt', encoding="utf-8") as f:  # create a file object
#     # could also read a few lines with f.readline()
#     my_lines = [line.rstrip() for line in f]
# # # # # # # # # # # # #     # 99.9%  of time newline ends with /n
# # #
# print(my_lines[:5])
# # #
# # # # # # # # # super precise only strip newlines from right side
# # # # # # # # with open('frost.txt', encoding="utf-8") as f:  # create a file object
# # # # # # # #     # could also read a few lines with f.readline()
# # # # # # # #     mylines = [line.rstrip('\n') for line in f]
# # # # # # # #     # 99.9%  of time newline ends with \n
# # #
# # # # # # # # print(mylines[:5])
# # #
# needle = "roads"  # what i want to find
# # # # # # # # # with open('Diena_12_Faili/frost.txt', encoding="utf-8") as f:  # create a file object
# with open('frost.txt', encoding="utf-8") as f:  # create a file object
#     # filtered_lines = [line for line in f if needle in line]
#     #     # i cant do second loop without seek
#     #     # same as above list comprehension
#     # for more complex filtering
#     filtered_lines = []
#     for line in f:
#         if needle in line:
#             filtered_lines.append(line)
# #
# print(filtered_lines)
# # # # # # # # # # # # #         # could also read a few lines with f.readline()
# # # # # # # # # #     # remember that going through file again would require f.seek(0)
# # # #     # filtered_lines_num = [(i, line.rstrip('\n'))
# # # #     #                   for i, line in enumerate(f, start=1) if "roads" in line]
# # #
# # # print(filtered_lines)
# # # # # # i want to save my filtered lines
# # # # # # mode = w will overwrite old fiile, no error
# now = dt.now()  # timestampe fixed here
# print(now)
# # # # # # # timestamp in file name
# file_path = Path("frost_cleaned_a4.txt")
# # file_path = Path(f"frost_{needle}_{now.month}_{now.day}_{now.hour}_{now.minute}_{now.second}.txt")
# print(file_path)
# print(file_path.stem)  # without extension this is offer by Path
# print(file_path.suffix) # extension
# # #
# # if file_path.is_file(): # this is offered by Path from standard library module pathlib
# #     print(f"Sorry {file_path} exists, so not going to overwrite") # should be very rare once a year ...
# # else:  # so file does not exist
# #     with open(file_path, mode="w", encoding="utf-8") as file_out:
# #         print(f"Writing {len(filtered_lines)} lines into {file_path}")
# #         file_out.writelines(filtered_lines)  # write lines to file, you need to make sure \n is there
# # #
# # # # with open('frost.txt', encoding="utf-8") as f:  # create a file object
# # # #     # filtered_lines = [line for line in f if needle in line]
# # # # # # # # # # # # #     # so only get 3rd and 4th token from each line if they are actual tokens to be gotten
# # # #     # filtered_lines = [line.split()[2:4] for line in f if len(line.split()) > 3]
# # # #     # filtered_lines = [line.rstrip('\n')
# # # #     #                   for line in f if line.startswith("And")]  # possible to use regex from re
# # # #     # filtered_lines = [line for line in f if line[0] in string.digits] # so only lines which start with digits
# # # # # # # # # # # # # #     #     # possible to use regex from re
# # # # # # # # # # # # # #     #     filtered_lines = [line for line in f if line.startswith("And")]
# # # # # # # # # # # # # #     # for more difficult filtering:
# # # #     filtered_lines = []
# # # #     for line in f:
# # # #         if line.startswith("And"):
# # # #             filtered_lines.append(line.rstrip())
# # # # print(filtered_lines)
# # # # # print(filtered_lines)
# # # # # # # # # print(filtered_lines_num)
# # #
# # # # # # # # # # # # # how to write a file?
# # # # # # # # # # # # # with mode = "w" file will be created or overwritten
# file_path = Path("frost-filtered.txt")
# # with open(file_path, mode="w", encoding="utf-8") as f:
# #     f.write("My filtered file\n")
# #     f.write("\n"*2) # two empty lines
# #     f.writelines(filtered_lines)  # remember to check if you need \n
# #     f.writelines([line+"\n" for line in filtered_lines]) # including last one
# #     f.write("*"*40+"\n")
# #     f.write("\n".join(filtered_lines)) # without newline in last line
# #     f.write("*"*40+"\n")
# # #     f.write("".join(filtered_lines)) # without newline in last line
# # # # # # # # # # # # # # # file should be closed here, crucial for writing
# # # # # # # # import datetime
# # # # # # # # # mode="a" is for append to the file
# # # # now = dt.now()
# # # print("Now will append to ", file_path)
# with open(file_path, mode="a", encoding="utf-8") as f:
#     f.write("\n"+"*"*40+"\n")
# #
#     f.write(str(now)+"\n")  #wrote a timestamp into a file
#     for n in range(5):
#         f.write(f"{n}\n")
#     my_list = list("abba")
#     f.write("\n".join(my_list))  #another way how to add list elements in new lines
#     f.write("\n")
#     for line in filtered_lines:
#         f.write(line+"\n")
#     print("Printing into file using print", file=f)  # this requires that f is open of course
#     # print to stream will be slower than writing to file
#     # because print has to do some formatting - overhead
# # #
# # # # # # print(now.day, now.year, now.minute, now.second)
# # # # # now = dt.now()
# # # # # fname = f"fails_{now.month}_{now.day}_{now.hour}_{now.minute}_{now.second}.txt"
# # #
# # # # # # # # fname = f"fail_{now.ctime()}.txt" # : will mess the file name
# # # # # # # with open(fname, mode="w", encoding="utf-8") as f:
# # # # # # #       f.writelines(filtered_lines)
# # # # # # # # # # # # we will append to file
# # # # # # # # # # # # with open('frost-filtered.txt', mode="a", encoding="utf-8") as f:
# # # # # # # # # # # #     f.writelines(filtered_lines)
# # # # print(file_path)
# # # # # # # # # # # # open two files one for reading one for writing
# # # # # # # # # # # # this could be very useful for working with very large files > more than your RAM
# #
# # # # # # # # # with open('Diena_12_Faili/frost.txt', encoding="utf-8") as fin, open('frost-filtered.txt', mode="w",
# # # encoding="utf-8") as fout:

# so when we have big files they might not fit into memory - RAM
# so we need to read and write in chunks
# # recipe for opening and writing huge files as long as lines are not too long
# line/row is a string which ends with \n
# so imagine this frost.txt file is 1GB or even 10GB or 100GB
with open('frost.txt', encoding="utf-8") as fin, open("frost_a4.txt", mode="w", encoding="utf-8") as file_out:
    for line in fin:  # for each line in incoming file
        # will work even on huge files because you do not need to
        # store all in memory
        # if line.startswith("And"):  # check some condition could be very complicated
        if "and" in line:  # check some condition could be very complicated
            # we could do more text processing here
            file_out.write(line)  # write into outgoing file
# # so here both files will be closed and ready to be used
# # #
# # # # # # # with open('frost.txt', encoding="utf-8") as fin, open('frost-yelling.txt', mode="w", encoding="utf-8") as
# # # fout: # # # #     for line in fin:  # for each line in incoming file # # # #         fout.write(line.upper()) #
# # # keeping also the newlines
# # #
# # # # # # # # we can open files without with
# # # # # # # f = open('frost.txt', encoding="utf-8")
# # # # # # # for line in f:
# # # # # # #     print(line)
# # # # # # # f.close() # need to close manually
# # #
# # # # # # # with open('frost.txt', encoding="utf-8") as fin, open('frost-yelling.txt', mode="w", encoding="utf-8") as fout:
# # # # # # #     for line in fin:  # for each line in incoming file
# # # # # # #         if line[0] == "\n": # if line starts with "\n" means it is is just one character line
# # # # # # #             fout.write("*"*40+"\n")
# # # # # # #         else:
# # # # # # #             fout.write(line.upper()) # keeping also the newlines
# # # # # # # # both files are closed here
# # #
# # #
# # # # # # # # we can also open files in binary
# # # # # # # with open('frost.txt', mode='rb') as fbin:
# # # # # # #     res = fbin.read()
# # #
# # # # # # # print(res) # usually we would not print binary because there could be unprintable symbols there..
# # #
# # # # # # # # # we can convert bytes to integer (floats tooo) sākot no Python 3.2
# # # # # # # my_int_big = int.from_bytes(res[:4], byteorder="big")
# # # # # # # my_int_little = int.from_bytes(res[:4], byteorder="little")
# # # # # # # print(my_int_big, my_int_little)
# # #
# # #
# # # # # # # with open("print-tests.txt", encoding='utf-8', mode="w") as f:
# # # # # # #     print(f"Just some text random stuff", file=f)
# # #
# # #
# # # # # print(f"Will combine {len(current_text_files)}")
# # # # print(current_text_files)
# # # # big_file_path = Path("big_text.txt")
# # # # # # careful since we are going to add to itself same directory
# # # # all_but_big = [f for f in current_text_files if f != big_file_path]
# # # # print(len(current_text_files), len(all_but_big))
# # #
# # # # with open(big_file_path, mode="w", encoding="utf-8") as fout:
# # # #     fout.write(f"\n\n{now}\n\n".join([open(f, encoding="utf-8").read() for f in all_but_big]))

# Python open modes
# r - read - default
# w - write
# a - append
# r+ - read and write - not recommended
# w+ - write and read - not recommended
# a+ - append and read - not recommended
# b - binary
# t - text - default
# + - read and write
# documentation https://docs.python.org/3/library/functions.html#open

# using Path read current absolute path
print(Path().absolute()) # empty parameters are the current path
# alternative to get current path with os module 
print(os.getcwd())

# prints the same but Path version will handle OS specific path separators better


# reading data from website is a big topic which we will handle later
# for now we will just read some text file from the web
url = "https://www.gutenberg.org/files/1661/1661-0.txt"
# read file from url using standard library

import urllib.request # this is a standard library
# i had to import request module from urllib library
# i use with to automatically close the connection when I am done
with urllib.request.urlopen(url) as response:
    text = response.read().decode("utf-8")
print(text[:1000])
# now I can save text to file
with open("sherlock.txt", mode="w", encoding="utf-8") as f:
    f.write(text)