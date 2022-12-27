# --- Day 3: Perfectly Spherical Houses in a Vacuum ---
def load_puzzle() -> list:
    data = list()
    with open("puzzle_input.txt") as file:
        data = list(file.readline())
    return data

class Santa:

    def __init__(self, name :str) -> None:
        self.x :int = 0
        self.y :int = 0
        self.name :str = name
        self.visited :dict = dict()
        self.visited["0,0"] = 1

    def visit(self, direction :str):
        if direction == ">":
            self.x += 1
        elif direction == "<":
            self.x -= 1
        elif direction == "^":
            self.y += 1
        elif direction == "v":
            self.y -= 1
        
        key = ",".join([ str(i) for i in self.get_position() ])

        try:
            self.visited[key] += 1
        except Exception as e:
            self.visited[key] = 1

    def get_position(self) -> list:
        return [self.x, self.y]

    def get_house_count(self) -> int:
        return len(self.visited)

    def __str__(self) -> str:
        return "%s @ %s" % (self.name, self.get_position())


def part_one_solution():
    data = load_puzzle()
    santa = Santa("Santa")

    # Solution for Part One of puzzle
    for direction in data:
        santa.visit(direction)

    print("Part one solution:", santa.get_house_count())


def part_two_solution():
    data = load_puzzle()

    santa = Santa("Santa")
    robot = Santa("Robot-Santa")
    current_person = santa

    for direction in data:
        # print(current_person)
        current_person.visit(direction)

        if current_person == santa:
            current_person = robot
        else:
            current_person = santa

    # print("santa has visited %s" % (santa.get_house_count()))
    # print("robot santa has visited %s" % (robot.get_house_count()))

    unique_houses = list()
    unique_houses.extend(list(set(list(santa.visited.keys()))))
    unique_houses.extend(list(set(list(robot.visited.keys()))))
    print("Part two solution:", len(list(set(unique_houses))))

part_one_solution()
part_two_solution()