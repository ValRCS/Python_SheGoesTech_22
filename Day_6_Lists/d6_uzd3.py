#3
# txt="Alus kauss mans"
# txt = input("Enter a sentence :")
# y=[]  # y is not strictly requird, we just show the original word order
# z=[]
# for word in txt.split():
#     y.append(word)
#     z.append(word[::-1].lower())
# new_txt = " ".join(z).capitalize()
# print(new_txt)
# print("OG", y)
# print("reversed and lowered", z)

print("\n___________Exercise 3 ________________\n")

user_input_text = input("enter some text: ")

list_of_words = user_input_text.split()
list_of_reversed_words = [word[::-1] for word in list_of_words]
reversed_text = ' '.join(list_of_reversed_words).capitalize()
print(reversed_text)