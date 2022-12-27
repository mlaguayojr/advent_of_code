# --- Day 1: Not Quite Lisp ---
def load_puzzle() -> list:
    data = list()
    with open("puzzle_input.txt") as f:
        data = [x for x in f.read()]
    return data

class Building:

    def __init__(self) -> None:
        self.floor_number :int = 0

    def up_floor(self):
        self.floor_number += 1
    
    def down_floor(self):
        self.floor_number -= 1

    def in_basement(self) -> bool:
        return self.floor_number < 0

    def __str__(self) -> str:
        return "Current floor: %i" % (self.floor_number)

def part_one_solution():
    data = load_puzzle()

    building = Building()
    for i in data:
        if i == "(":
            building.up_floor()
        elif i == ")":
            building.down_floor()
    
    print("Part one solution:", building.floor_number)

def part_two_solution():
    data = load_puzzle()

    building = Building()
    for index in range(0, len(data)):
        instruction = data[index]

        if instruction == "(":
            building.up_floor()
        elif instruction == ")":
            building.down_floor()

        if building.in_basement():
            break

    print("Part two solution:", index+1)


part_one_solution()
part_two_solution()