class Song:
    def __init__(self, title, author, lyrics):
        self.title = title
        self.author = author
        self.lyrics = lyrics
        print(f"{title} by {author} - created {len(self.lyrics)} lines")

    # _ significies that this method is for internal use by the other methods in the object
    def _print_lyrics(self, lyrics, max_lines=-1):  # these lyrics will be processed already
        if max_lines == -1:
            max_lines = len(lyrics)
        for i in lyrics[:max_lines]:
            print(i)
        # we could return self here as well

    def sing(self, max_lines=-1):
        # self.max_lines = max_lines
        print(f" Singing {self.title} - {self.author}")
        self._print_lyrics(self.lyrics, max_lines)
        return self

    def yell(self, max_lines=-1):
        capital_lyrics = [line.upper() for line in self.lyrics]
        print(f"YELLING {self.title} - {self.author}")
        self._print_lyrics(capital_lyrics, max_lines)
        return self


ziemelmeita = Song("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu", "Garu, tālu ceļu veicu"])
ziemelmeita.sing(1).yell()

vairogi = Song("Vairogi", "Līvi", ["Mūsu dziesmas ir vairogi seni", "Mēs tās par pagalvjiem liksim",
                                   "Daudzu likteņu pilni mēs elposim", "Kā pakalni Daugavas krastos"])
vairogi.sing(2).yell(1)

vairogi.sing().sing().sing()


class Rap(Song):

    # no need for custom __init__ in this case
    def break_it(self, max_lines=-1, drop="yeah"):
        print("Singer:", self.author, "-", self.title)
        for line in self.lyrics:
            print(line.replace(' ', f' {drop} '), sep="\n")
            max_lines -= 1
            if max_lines == 0:
                break
        return self


ziemelmeita = Rap("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu", "Garu, tālu ceļu veicu"])
ziemelmeita.break_it(1).break_it()

ziemelmeita.sing().yell().break_it()

livi = Rap("Vairogi", "Līvi", ["Mūsu dziesmas ir vairogi seni", "Mēs tās par pagalvjiem liksim",
                                   "Daudzu likteņu pilni mēs elposim", "Kā pakalni Daugavas krastos"])

livi.sing().yell(2).break_it(drop="Jā!").break_it(2, "ahh")

