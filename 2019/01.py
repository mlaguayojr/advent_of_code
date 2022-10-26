# --- Day 1: The Tyranny of the Rocket Equation ---
from math import floor

# Get puzzle input
data = list()
with open("puzzle_input.txt") as f:
    data = f.readlines()

def part_one_solution():
    """
    solution for part one
    """

    def get_fuel_required(mass :int) -> int:
        return floor( (mass/3) ) - 2

    total = 0
    for i in data:
        total += get_fuel_required(int(i.strip()))
    print(total)

def part_two_solution():
    """
    solution for part two
    """
    
    def get_fuel_required(mass :int) -> int:
        fuel = floor( (mass/3) ) - 2

        if fuel <= 0:
            return 0
        else:
            return (fuel + get_fuel_required(fuel) )

    total = 0
    for i in data:
        total += get_fuel_required(int(i.strip()))
    print(total)

part_one_solution()
part_two_solution()