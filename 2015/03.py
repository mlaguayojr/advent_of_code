# --- Day 3: Perfectly Spherical Houses in a Vacuum ---

puzzle = None

with open("puzzle_input.txt") as file:
    puzzle = file.readline()

class Santa:

    def __init__(self, name :str) -> None:
        self.x = 0
        self.y = 0
        self.name = name
        self.visited = dict()
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
        
        key = ",".join([ str(i) for i in self.getPosition() ])

        try:
            self.visited[key] += 1
        except Exception as e:
            self.visited[key] = 1

    def getPosition(self) -> list:
        return [self.x, self.y]

    def getHouseCount(self) -> int:
        return len(self.visited)

    def __str__(self) -> str:
        return "%s @ %s" % (self.name, self.getPosition())

santa = Santa("Santa")

# Solution for Part One of puzzle
for direction in range(0, len(puzzle)):
    direction = puzzle[direction]
    santa.visit(direction)

print("santa has visited %s" % (santa.getHouseCount()))


# Solution for Part Two of puzzle
santa = Santa("Santa")
robot = Santa("Robot-Santa")
current_person = santa

for direction in range(0, len(puzzle)):
    direction = puzzle[direction]

    print(current_person)
    current_person.visit(direction)

    if current_person == santa:
        current_person = robot
    else:
        current_person = santa

print("santa has visited %s" % (santa.getHouseCount()))
print("robot santa has visited %s" % (robot.getHouseCount()))

unique_houses = list()
unique_houses.extend(list(set(list(santa.visited.keys()))))
unique_houses.extend(list(set(list(robot.visited.keys()))))
print(len(list(set(unique_houses))))