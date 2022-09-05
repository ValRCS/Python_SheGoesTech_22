# width_str = input("input width - meters")
# length_str = input("input length - meters")
# height_str = input("input height - meters")
# # w, l, h would be fine as variables here
#
# width_fl = float(width_str)
# length_fl = float(length_str)
# height_fl = float(height_str)

w = float(input("input width - meters"))
l = float(input("input length - meters"))
h = float(input("input height - meters"))

room_size = w * l * h
# print(f"Room size = {room_size} m\u00B3")
print(f"Room size = {room_size} m³")