# we will create an App class that inherits from the Tk class
# this approach can be seen in tkinter documentation
# https://docs.python.org/3/library/tkinter.html#tkinter.Tk

import tkinter as tk

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

        # add a textview
        self.textview = tk.Text()
        # add a color to the textview
        self.textview.config(fg="yellow", bg="blue")
        # attach the textview to the bottom frame
        self.textview.pack(in_=self.bottom_frame, side=tk.TOP, pady=10)



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

    # TODO add a method to open a file for now just the default file
    # file contents should be displayed in the textview

    # TODO later on we will explore how to open any file - you can try looking up the filedialog module
    # https://docs.python.org/3/library/tkinter.filedialog.html

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
        self.file_menu.add_command(label="Open") # TODO add a binding to a function
        # add a close option
        self.file_menu.add_command(label="Close") # TODO add a binding to a function
        # add a save option
        self.file_menu.add_command(label="Save", command=self.save_file) # TODO add a binding to a function


        # add a save as option
        self.file_menu.add_command(label="Save As") # TODO add a binding to a function
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