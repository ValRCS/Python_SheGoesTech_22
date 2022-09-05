# def get_file_len(file_name):
#     with open(file_name) as f:
#         file_len = len(f.readlines())
#     # file is closed automatically
#     return file_len

import string


def get_file_len(file_name):
    file_len = 0
    with open(file_name, encoding="UTF-8") as f:
        for _ in f:  # will work even on large files
            file_len += 1
    return file_len


print(get_file_len('day12_u1.py'))
print(get_file_len('veidenbaums.txt'))


# def get_poem_lines(file_name):
#     poem_lines = []
#     with open(file_name, encoding="UTF-8") as f:
#         for line in f:
#             if line.strip() and "***" not in line:  # line has to have some content and not contain ***
#                 poem_lines.append(line)
#     return poem_lines


def get_poem_lines(fpath):
    with open(fpath, encoding="utf-8") as fstream:
        lines = (line.rstrip() for line in fstream if
                 not line.__contains__("***"))  # getting rid of whitespace and *** lines
        lines = list(line for line in lines if line)
        return lines


print(len(get_poem_lines('veidenbaums.txt')))


# def save_lines(lines, file_name):
#     with open(file_name, "w", encoding="UTF-8") as f:
#         for line in lines:
#             f.write(line + "\n")


def save_lines(destpath, lines, encoded="UTF-8", endline="\n"):
    with open(destpath, mode="w", encoding=encoded) as f:
        f.write(endline.join(lines))  # so each line is separated by endline


# save_lines("veidenbaums_clean.txt", get_poem_lines("veidenbaums.txt"))  # one liner
poem_lines = get_poem_lines("veidenbaums.txt")
save_lines("veidenbaums_clean.txt", poem_lines)


# 1e -> write the function clean_punkts (srcpath, destpath)
# function will open the srcpath file, clear it from https://docs.python.org/3/library/string.html#string.punctuation
# then function will save the cleaned text into destpath

def clean_punkts(srcpath, destpath, bad_chars=string.punctuation, encoded="UTF-8"):
    with open(srcpath, mode="r", encoding=encoded) as src_file, open(destpath, mode="w", encoding=encoded) as dest_file:
        text = src_file.read()
        for p in bad_chars:
            text = text.replace(p, "")  # we replace each bad char with empty string
        dest_file.write(text)


# clean_punkts("veidenbaums_clean.txt", "veidenbaums_clean_punkts.txt")
clean_punkts("veidenbaums_clean.txt", "veidenbaums_clean_punkts.txt", bad_chars=string.punctuation + "…")
