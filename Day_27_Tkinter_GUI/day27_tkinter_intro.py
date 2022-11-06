# what is Tkinter?
# Tkinter is a standard GUI library for Python.
# Python when combined with Tkinter provides a fast and easy way to create GUI applications.

# Tkinter provides a powerful object-oriented interface to the Tk GUI toolkit.
# documentation: https://docs.python.org/3/library/tk.html

# external tutorial at Real Python
# https://realpython.com/python-gui-tkinter/

# examples of tkinter applications:
# thonny IDE - https://thonny.org/

# for more commercial applications:
# https://www.tcl.tk/software/tkinter/
# usually tkinter is used for small applications - internal tools for companies etc
# for bigger more professional applications, other GUI frameworks are used
# such as QT based frameworks, Kivy, etc.

# import 
import tkinter as tk # some tutorials use * but that is not recommended because it can cause name conflicts

# window = tk.Tk() # create a window object - this is the main window of the application
window = tk.Tk(className="My First GUI Program") # create a window with a title

# widgets are commonly used in GUI applications
# examples of widgets:
# buttons, labels, text boxes, radio buttons, check boxes, etc

# create a label widget - object just like anything else in Python
label = tk.Label(text="Hello, Tkinter from Python")
# we need to attach the label to the window
# easiest way is to use pack() method
label.pack()
# when packing the label, it will be placed in the center of the window
# window will be resized to fit the label

# add a color to the label
label.config(fg="yellow", bg="blue")

# adjust window size
window.minsize(width=500, height=300)

# add a plus button
button_plus = tk.Button(text="+")
button_plus.pack()



# create a label to display the counter
counter_label = tk.Label(text="0")
counter_label.pack()

# create a function to increase the counter
def increase_counter():
    # get the current value of the counter
    current_value = int(counter_label["text"])
    # increase the value by 1
    new_value = current_value + 1
    # update the label with the new value
    counter_label.config(text=str(new_value))

# bind the button to the function after creating it
button_plus.config(command=increase_counter)

def decrease_counter():
    # get the current value of the counter
    current_value = int(counter_label["text"])
    # increase the value by 1
    new_value = current_value - 1
    # update the label with the new value
    counter_label.config(text=str(new_value))

# add a minus button and bind it to a function immediately
button_minus = tk.Button(text="-", command=decrease_counter)
# pack the minus button
button_minus.pack()

# TODO create a layout with 3 buttons - plus, minus, reset
# TODO create a function to reset the counter to 0
# TODO bind the reset button to the function


# run window main loop
window.mainloop()
# input("Press any key to continue...") # wait for user input