# --- Day 4: The Ideal Stocking Stuffer ---
from hashlib import md5

def load_puzzle() -> str:
    data = ""
    with open("puzzle_input.txt") as f:
        data = f.readline()
    return data.strip()

def get_hash(input :str) -> str:
    return md5(input.encode('utf-8')).hexdigest()


def part_one_solution():
    data = load_puzzle()
    found = False
    number = 0

    while not(found):
        hash = get_hash("".join([data, str(number)]))
        found = hash.startswith("0"*5)
        
        if not found:
            number += 1

    print("Part one solution:", number)

def part_two_solution():
    data = load_puzzle()
    found = False
    number = 0

    while not(found):
        hash = get_hash("".join([data, str(number)]))
        found = hash.startswith("0"*6)
        
        if not found:
            number += 1

    print("Part two solution:", number)

part_one_solution()
part_two_solution()