# --- Day 3: Rucksack Reorganization ---
def load_puzzle_input() -> list:
    data = list()
    with open("puzzle_input.txt") as f:
        data = [ x.strip('\n') for x in f.readlines() ]
    return data

def is_between(min_value :int, value :int, max_value :int) -> bool:
    check1 = min_value <= value
    check2 = value <= max_value
    return check1 and check2

class Rucksack:

    def __init__(self) -> None:
        self.compartment_one = str()
        self.compartment_two = str()

    def add_items(self, items :str,) -> None:
        half_way = int(len(items)/2)
        self.compartment_one = items[0:half_way]
        self.compartment_two = items[half_way:]

    def shared_items(self) -> list:
        same_items = []
        list_one = list(set(self.compartment_one))
        list_two = list(set(self.compartment_two))

        for x in list_one:
            if x in list_two:
                same_items.append(x)
        return same_items

    def collective_shared_items(self, items :list) -> list:
        shared_items = list()

        unique_letters = list(set(list("".join(items))))
        
        for character in unique_letters:

            if (
                (character in items[0])
                and (character in items[1])
                and (character in items[2])
            ):
                shared_items.append(character)

        return shared_items

    def calc_points(self, shared_items :list) -> int:
        points = 0

        for x in shared_items:
            num_value = ord(str(x))

            if is_between(1, num_value - 96, 26):
                points += num_value - 96
            
            elif is_between(27, num_value - 38, 52):
                points += num_value - 38

        return points

    def __str__(self) -> str:
        return "L: %s, R: %s" % (self.compartment_one, self.compartment_two)


def part_one_solution():
    data = load_puzzle_input()
    points = 0

    for i in data:
        bag = Rucksack()
        bag.add_items(i)
        shared_items = bag.shared_items()
        points += bag.calc_points(shared_items)
    
    print("Part One:", points)

def part_two_solution():
    data = load_puzzle_input()
    points = 0

    for x in range(0, len(data), 3):                
        bag_one = Rucksack()
        shared_items = bag_one.collective_shared_items(data[x:x+3])
        points += bag_one.calc_points(shared_items)
    
    print("Part Two:", points)

part_one_solution()
part_two_solution()