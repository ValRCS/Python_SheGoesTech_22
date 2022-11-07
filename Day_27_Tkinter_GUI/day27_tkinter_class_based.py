# we will create an App class that inherits from the Tk class
# this approach can be seen in tkinter documentation
# https://docs.python.org/3/library/tkinter.html#tkinter.Tk
import tkinter.filedialog
import tkinter.scrolledtext

import tkinter as tk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import string

# so my App inherits from the Tk class
class App(tk.Tk):

    # constructor - things that happen when the object is created
    def __init__(self, width=500, height=300, title="Our second GUI Program", default_save_file="default.txt"):
        # first we need to call the parent constructor - the Tk class
        super().__init__() # remember this from our class lecture on inheritance?

        # add a title to the window
        self.title(title)
        # set the minimum size of the window
        self.minsize(width=width, height=height)

        # add a default save file
        self.default_save_file = default_save_file

        # call the method to setup widgets
        self._setup_widgets()

        # setup the menus
        self._setup_menus()



    # method to setup widgets
    def _setup_widgets(self):
        # let's setup up some frames
        # we will have a top frame and a bottom frame
        # the top frame will have a label and a button

        # create a top frame
        self.top_frame = tk.Frame()
        # set background color
        self.top_frame.config(bg="aquamarine")
        # pack the frame
        self.top_frame.pack(fill=tk.BOTH, expand=True)

        # create a middle frame
        self.middle_frame = tk.Frame()
        # set background color - out of 24 million colors
        self.middle_frame.config(bg="#708090") # so to set colors by numbers we use # and then the hex code
        #set frame size
        self.middle_frame.config(width=500, height=200)
        # pack the frame
        self.middle_frame.pack(fill=tk.BOTH, expand=True)

        # create a bottom frame
        self.bottom_frame = tk.Frame()
        # set background color
        self.bottom_frame.config(bg="lightblue")
        # pack the frame
        self.bottom_frame.pack(fill=tk.BOTH, expand=True)

        # create a label widget
        self.label = tk.Label(text="Hello, Tkinter from Python")
        # add a color to the label
        self.label.config(fg="yellow", bg="blue")
        # attach the label to the top frame
        self.label.pack(in_=self.top_frame, side=tk.TOP, pady=10)

        # create clear button with a command to be called when the button is clicked
        self.clear_button = tk.Button(text="Clear Text", command=self.clear_text)
        # attach the button to the top frame
        self.clear_button.pack(in_=self.top_frame, side=tk.LEFT, padx=10, pady=10)

        # create a button widget to calculate word count
        self.word_count_button = tk.Button(text="Word Frequencies", command=self.word_frequency)
        # attach the button to the top frame
        self.word_count_button.pack(in_=self.top_frame, side=tk.BOTTOM, padx=10, pady=10)

        # let's add an upper case button and the command to be called when the button is clicked
        self.upper_button = tk.Button(text="Upper Case", command=self.upper_case)
        # attach the button to the top frame
        self.upper_button.pack(in_=self.top_frame, side=tk.RIGHT, padx=10, pady=10)

        # create a figure for the matplotlib graph

        # create a figure
        self.figure = plt.Figure(figsize=(5,4), dpi=100)
        # add a subplot
        self.subplot = self.figure.add_subplot(111)
        # create FigureCanvasTkAgg object
        self.canvas = FigureCanvasTkAgg(self.figure, self.middle_frame)
        # pack it
        self.canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # add a textview that can be scrolled
        # create a scrollbar
        # self.scrollbar = tk.Scrollbar() # we would have to add the bindings to the scrollbar
        # attach the scrollbar to the bottom frame
        # self.scrollbar.pack(in_=self.bottom_frame, side=tk.RIGHT, fill=tk.Y)
        # create a textview
        # instead lets use Scrolled Text widget


        # self.textview = tk.Text()
        self.textview = tkinter.scrolledtext.ScrolledText()
        # add a color to the textview
        self.textview.config(fg="yellow", bg="blue")
        # attach the textview to the bottom frame
        self.textview.pack(in_=self.bottom_frame, side=tk.TOP, pady=10)

        # what other widgets can we add?

        # list of tkinter widgets
        # https://docs.python.org/3/library/tkinter.html#widgets



        # add a quit button
        # self.button_quit = tk.Button(text="Quit", command=self.quit)
        # # self.quit is provided by the Tk class - we did not have to create it
        # self.button_quit.pack()
        # create a method to save the file
    def save_file(self):
        
        # get the text from the textview
        text = self.textview.get("1.0", tk.END)
        # open the file
        with open(self.default_save_file, "w", encoding="utf-8") as file:
            # write the text to the file
            file.write(text)

    def save_file_with_dialog(self):
        # open a file dialog
        # we can use the asksaveasfilename method
        # this method returns the path to the file
        # alias tk will not work
        # https://stackoverflow.com/questions/45533932/python-3-6-attributeerror-module-tkinter-has-no-attribute-filedialog
        file_path = tkinter.filedialog.asksaveasfilename()
        # get the text from the textview
        text = self.textview.get("1.0", tk.END)
        # open the file
        with open(file_path, "w", encoding="utf-8") as file:
            # write the text to the file
            file.write(text)
            print(f"File saved to {file_path}")

    # TODO add a method to open a file for now just the default file
    # file contents should be displayed in the textview
    def open_file(self):
        # open the file
        with open(self.default_save_file, "r", encoding="utf-8") as file:
            # read the text from the file
            text = file.read()
            # set the text in the textview
            # self.textview.delete("1.0", tk.END)
            # insert text at the beginning of the textview
            # self.textview.insert("1.0", text)
            # we insert at the end of the text
            self.textview.insert(tk.END, text) # this will keep appending each time we open the file

    def clear_text(self):
        # clear the textview
        self.textview.delete("1.0", tk.END)

    def open_file_with_dialog(self):
        # open a file dialog
        # we can use the askopenfilename method
        # this method returns the path to the file
        file_path = tkinter.filedialog.askopenfilename()
        # open the file
        with open(file_path, "r", encoding="utf-8") as file:
            # read the text from the file
            text = file.read()
            # set the text in the textview
            # self.textview.delete("1.0", tk.END)
            self.clear_text() # we can use the method we created just like above text
            # insert text at the beginning of the textview
            self.textview.insert("1.0", text)
    # https://docs.python.org/3/library/tkinter.filedialog.html

    def upper_case(self):
        # get the text from the textview
        text = self.textview.get("1.0", tk.END)
        # convert the text to upper case
        text = text.upper()
        # set the text in the textview
        self.textview.delete("1.0", tk.END)
        self.textview.insert("1.0", text)


    def word_frequency(self):
        # get the text from the textview
        text = self.textview.get("1.0", tk.END)
        # convert the text to lower case
        text = text.lower()
        # remove punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))
        # split the text into words
        words = text.split()
        # create a dictionary to store the word frequencies
        word_frequencies = {}
        # loop through the words
        for word in words:
            # check if the word is in the dictionary
            if word in word_frequencies:
                # increment the count
                word_frequencies[word] += 1
            else:
                # add the word to the dictionary
                word_frequencies[word] = 1
        # sort the dictionary by value
        sorted_word_frequencies = sorted(word_frequencies.items(), key=lambda x: x[1], reverse=True)
        # get the top 10 words
        top_10_words = sorted_word_frequencies[:10]
        # get the words
        words = [word for word, count in top_10_words]
        # get the counts
        counts = [count for word, count in top_10_words]
        # clear the figure
        self.figure.clear()
        # add a subplot
        self.subplot = self.figure.add_subplot(111)
        # plot the graph
        self.subplot.bar(words, counts)
        # refresh the canvas
        self.canvas.draw()

    def _setup_menus(self):
        # add a menu with a quit option
        self.menu = tk.Menu()

        # we add a quit option to the menu
        # self.menu.add_command(label="Quit", command=self.quit)
        # add the menu to the window
        self.config(menu=self.menu)

        # let's add a file menu
        self.file_menu = tk.Menu()
        # add a new option to the file menu
        self.file_menu.add_command(label="New") # TODO add a binding to a function
        # add a separator
        self.file_menu.add_separator()
        # add an open option
        self.file_menu.add_command(label="Open", command=self.open_file_with_dialog) 
        self.file_menu.add_command(label="Open and Append Default", command=self.open_file) 
        # add a close option
        self.file_menu.add_command(label="Close") # TODO add a binding to a function
        # add a save option
        self.file_menu.add_command(label="Save Default", command=self.save_file) 


        # add a save as option
        self.file_menu.add_command(label="Save As", command=self.save_file_with_dialog) 
        # add a separator
        self.file_menu.add_separator()
        # add an exit option
        self.file_menu.add_command(label="Exit", command=self.quit)

        # add file_menu to the menu bar
        # self.config(menu=self.file_menu)
        
        # add the file menu to the menu bar
        self.menu.add_cascade(label="File", menu=self.file_menu) # this was under hierarchy under menu

        # let's add about and help menus
        self.about_menu = tk.Menu()
        # let's add help
        self.about_menu.add_command(label="Help") # TODO add a binding to a function
        # add an about option
        self.about_menu.add_command(label="About") # TODO add a binding to a function

        # add the about menu to the menu bar
        self.menu.add_cascade(label="About", menu=self.about_menu) # this was under hierarchy under menu



# finally add a main function
def main():
    # create an App object which is an instance of the App class
    app = App()
    # run the main loop
    app.mainloop()

# run the main function
# main() # this approach would be okay if we had no plans for importing this module

# instead better is to use a main guard
if __name__ == "__main__":
    # we could run some configuration code here
    main()
    # we could run some cleanup code here


# for games there is specific pygame library for games
# https://www.pygame.org/news