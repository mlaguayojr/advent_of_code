# --- Day 2: I Was Told There Would Be No Math ---
def load_puzzle() -> list:
    data = list()
    with open("puzzle_input.txt") as f:
        data = [ [int(y) for y in x.split("x") ] for x in f.readlines()]
    return data

class RightRectangularPrism:
    
    def __init__(self, dimensions :list) -> None:
        self.length :int = dimensions[0]
        self.width :int = dimensions[1]
        self.height :int = dimensions[2]
        self.dimensions :list(int) = dimensions

    def get_surface_area(self) -> int:
        return (
            (2 * self.length * self.width)
            + (2 * self.width * self.height)
            + (2 * self.height * self.length)
            + self.get_area_of_smallest_side()
        )

    def get_area_of_smallest_side(self) -> int:
        smallest = sorted(self.dimensions, reverse=False)[:2]
        return smallest[0] * smallest[1]

    def get_feet_of_ribbon(self) -> int:
        smallest_perimeter = min([
            (2 * self.height) + (2 * self.length), 
            (2 * self.width) + (2 * self.length),
            (2 * self.width) + (2 * self.height)
        ])
        
        return (
            smallest_perimeter
            + (self.length * self.width * self.height)
        )

    def __str__(self) -> str:
        return "L: %i, W: %i, H: %i" % (self.length, self.width, self.height)

def part_one_solution():
    data = load_puzzle()
    total_sum = 0

    for i in data:
        shape = RightRectangularPrism(i)
        total_sum += shape.get_surface_area()
    
    print("Part one solution:", total_sum)

def part_two_solution():
    data = load_puzzle()
    total_sum = 0

    for i in data:
        shape = RightRectangularPrism(i)
        total_sum += shape.get_feet_of_ribbon()
    
    print("Part two solution:", total_sum)

part_one_solution()
part_two_solution()