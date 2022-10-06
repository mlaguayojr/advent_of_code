# --- Day 6: Probably a Fire Hazard ---

class Point:

    def __init__(self, row :int, column :int):
        self.row = row
        self.column = column

    def __eq__(self, o) -> bool:
        return (
            (self.row == o.row)
            and (self.column == o.column)
        )

    def __str__(self) -> str:
        return "(%i, %i)" % (self.row, self.column)

    def __repr__(self) -> list:
        return [self.row, self.column]


class Grid:

    def __init__(self, rows :int, columns :int):
        self.grid = list( [0] * rows)
        
        for row in range(0, rows):
            self.grid[row] = list([0]*columns)
    
    def __str__(self):
        line = ""
        
        for rows in self.grid:

            for col in rows:
                if col == 0:
                    line += ""
                else:
                    line += "."
            
            line += "\n"
        
        return line

    def set_light(self, row :int, column :int, value :int):
        # print("before: ", get_light(row, column))
        self.grid[row][column] = value
        # print("after: ", get_light(row, column))

    def get_light(self, row :int, column :int) -> int:
        return self.grid[row][column]

    def get_points(self, start_point :Point, end_point :Point) -> list:
        points = list()

        current_point = Point(start_point.row, start_point.column)
        # print(current_point, "->", end_point)

        while(current_point != end_point):
            points.append(Point(current_point.row, current_point.column))
            
            if current_point.column != end_point.column:
                current_point.column += 1
            else:
                current_point.column = 0
                current_point.row += 1

        points.append(Point(end_point.row, end_point.column))
        return points

class Instruction:

    def __init__(self, line :str):
        [part_one, part_two] = line.split(" through ")
        part_one = part_one.strip()

        valid_commands = ["turn off", "turn on", "toggle"]

        self.command = None

        for i in valid_commands:
            if part_one.startswith(i):
                self.command = i
                break
        
        part_one = part_one.replace(self.command, "").strip()
        [row, column] = [ int(x) for x in part_one.split(',') ]
        self.start_point = Point(row, column)
        
        [row, column] = [ int(x) for x in part_two.split(',') ]
        self.end_point = Point(row, column)

if __name__=="__main__":

    # Get data
    data = []
    with open("puzzle_input.txt") as f:
        data = f.readlines()

    # Create grid
    grid = Grid(1000, 1000)

    # Follow instructions
    for line in data:
        ins = Instruction(line.rstrip())

        points = grid.get_points(ins.start_point, ins.end_point)

        for point in points:
            if ins.command == "turn on":
                grid.set_light(point.row, point.column, 1)
            elif ins.command == "turn off":
                grid.set_light(point.row, point.column, 0)
            elif ins.command == "toggle":
                current_value = grid.get_light(point.row, point.column)

                if current_value == 0:
                    current_value = 1
                else:
                    current_value = 0

                grid.set_light(point.row, point.column, current_value)
            else:
                continue

    lights_lit = 0
    for i in grid.grid:
        lights_lit += sum(i)
    
    print(grid)
    print(lights_lit)
