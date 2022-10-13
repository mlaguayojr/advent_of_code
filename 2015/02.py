# --- Day 2: I Was Told There Would Be No Math ---

puzzle = None

with open("puzzle_input.txt") as file:
    puzzle = file.readlines()

# Solution for Part One of puzzle
def surface_area(length :int, width :int, height :int) -> int:
    num1 = length * width
    num2 = width * height
    num3 = height * length
    surface_area = (2 * num1) + (2 * num2) + (2 * num3)
    return surface_area + min(num1, num2, num3)

total_surface_area = 0

for measurement in puzzle:
    [length, width, height] = [ int(i) for i in measurement.split("x") ]
    total_surface_area += surface_area(length, width, height)

print("puzzle one answer: %s" % (total_surface_area))

total_surface_area = 0 # reset

# Solution for Part Two of puzzle
def smallest_perimeter(length :int, width :int, height :int) -> int:
    face1 = (2 * height) + (2 * length)
    face2 = (2 * width) + (2 * length)
    face3 = (2 * width) + (2 * height)
    return min(face1, face2, face3)

for measurement in puzzle:
    [length, width, height] = [ int(i) for i in measurement.split("x") ]
    total_surface_area += ( smallest_perimeter(length, width, height) + (length *  width * height))

print("puzzle two answer: %s" % (total_surface_area))