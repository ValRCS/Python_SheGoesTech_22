# class Song:  # Song is name of Class, start with Capital letter
#     def __init__(self, title="", author="", lyrics=tuple()):  # constructor method called upon creation of object
#         self.title = title
#         self.author = author
#         self.lyrics = lyrics
#         # print(f"New Song made by Author: {self.author=}  Title: {self.title=}")
#
#     def sing(self):  # method definition which is function associated with objects
#         print(f"New Song Title:  {self.title}")
#         print(f"Lyrics made by Author: {self.author}")
#         for line in self.lyrics:
#             print(line)
#         return self
#
#     def yell(self):
#         for line in self.lyrics:
#             print(line.upper())
#         return self


# can be put inside the class or it's better to make _print_lyrics static inside the class?


class Song:
    def __init__(self, title, author, lyrics):
        self.title = title
        self.author = author
        self.lyrics = lyrics
        if title == '':
            title = 'Unknown'
        if author == '':
            author = 'Unknown'
        print(f"\n\nNew song made:\nTitle: {title} \nAuthor: {author}")

    @classmethod  # this means that this method is a class method can be called without any objects
    def print_lines(cls, lyrics, line_count=-1):
        all_lines_count = len(lyrics)
        if line_count == -1:
            line_count = len(lyrics)
        elif line_count <= 0:
            print("no lines to print")
        elif all_lines_count < line_count:
            print(f"only {all_lines_count} lines can be printed:\n")
        for i in lyrics[:line_count]:
            print(i)

    def sing(self, lines_present=-1):
        x = '_' * (len(self.author + self.title) + 3)
        print(x, '\nSinging:')
        self.print_lines(self.lyrics, lines_present)
        return self

    def yell(self, lines_present=-1):
        x = '_' * (len(self.author + self.title) + 3)
        lines_upper = [line.upper() for line in self.lyrics]
        print(x, '\nYELLING:')
        self.print_lines(lines_upper, lines_present)
        return self


class Rap(Song):
    def break_it(self, lines_present=-1, drop="yeah"):
        x = '_' * (len(self.author + self.title) + 3)
        lyrics = [line.replace(' ', f' {drop.upper()} ') + ' ' + drop.upper() for line in self.lyrics]
        print(x, '\nRapping:')
        self.print_lines(lyrics, lines_present)
        return self


ziemelmeita = Song('Ziemeļmeita', 'Jumprava', ['Gāju meklēt ziemeļmeitu', 'Garu, tālu ceļu veicu'])

ziemelmeita.sing(1).yell(10).sing().sing(-3)

zrap = Rap("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu", "Garu, tālu ceļu veicu"])

zrap.break_it(1, "yah").yell(1)

ziemelmeita.sing().yell().sing(1)

