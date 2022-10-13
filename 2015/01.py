# --- Day 1: Not Quite Lisp ---

puzzle = "" #define puzzle here

# Solution for Part One of puzzle
def count_floor(floor_letter: str) -> int:
    if floor_letter == "(":
        return 1
    elif floor_letter == ")":
        return -1

floor_number = 0
for index in range(0, len(puzzle), 1):
    letter = puzzle[index]
    # print( index + 1, letter)

    floor_number += count_floor(letter)

print("puzzle one answer: %s" % (floor_number))

floor_number = 0 # reset

# Solution for Part Two of puzzle
for index in range(0, len(puzzle), 1):
    letter = puzzle[index]
    # print( index + 1, letter)

    floor_number += count_floor(letter)

    if floor_number == -1:
        # print("entered the basement")
        floor_number = index + 1
        break

print("puzzle two answer: %s" % (floor_number))