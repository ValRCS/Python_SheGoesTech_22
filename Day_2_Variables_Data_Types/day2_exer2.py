#Ask user to input 3 numbers - width, length, height
width = input("Enter the width of the room in meters, please:\n")
length = input("Enter the length of the room in meters, please:\n")
height = input("Enter the height of the room in meters, please:\n")

#Find the volume of the room
#PS Think about units and what is the most appropriate data type for this
width = float(width) # no error handling here
length = float(length)
height = float(height)
volume = width * length * height
print(f"The volume of the room is {round(volume,2)} m\u00B3") # ³
print("\n")
