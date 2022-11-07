# we will create an App class that inherits from the Tk class
# this approach can be seen in tkinter documentation
# https://docs.python.org/3/library/tkinter.html#tkinter.Tk

import tkinter as tk

# so my App inherits from the Tk class
class App(tk.Tk):

    # constructor - things that happen when the object is created
    def __init__(self, width=500, height=300, title="Our second GUI Program"):
        # first we need to call the parent constructor - the Tk class
        super().__init__() # remember this from our class lecture on inheritance?

        # add a title to the window
        self.title(title)
        # set the minimum size of the window
        self.minsize(width=width, height=height)

        # create a label widget
        self.label = tk.Label(text="Hello, Tkinter from Python")
        # finally, pack the label
        self.label.pack()

        # add a color to the label
        self.label.config(fg="yellow", bg="blue")

        # add a quit button
        self.button_quit = tk.Button(text="Quit", command=self.quit)
        # self.quit is provided by the Tk class - we did not have to create it
        self.button_quit.pack()

        # add a menu with a quit option
        self.menu = tk.Menu()
        self.menu.add_command(label="Quit", command=self.quit)
        # add the menu to the window
        self.config(menu=self.menu)

# finally add a main function
def main():
    # create an App object
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