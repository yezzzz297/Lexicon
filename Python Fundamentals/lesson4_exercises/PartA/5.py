

def calculate_area(width, height):
    return width * height


room_width = 6
room_height = 4
area = calculate_area(room_width, room_height)

print(f"Area: {area} square units")
print(f"Perimeter estimate: {2 * (room_width + room_height)}")
