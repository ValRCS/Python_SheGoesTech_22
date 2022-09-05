# exercise 3
bad_text = input("Please input text: ")
# bad_text = "This cottage cheese is not so bad"
print(bad_text)
start_location = bad_text.find("not")
# print(start_location)
end_location = bad_text.find("bad")
end_word_len = len("bad")
# print(end_location)
good_str = ""
if end_location > start_location:
    good_str = (f"{bad_text[0:start_location]}good{bad_text[end_location+end_word_len:]}")  # TODO use end_location
else:
    good_str = bad_text
print(good_str)