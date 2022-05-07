# Day 4: The Ideal Stocking Stuffer

from hashlib import md5

puzzle = ""

def get_hash(input :str) -> str:
    return md5(input.encode('utf-8')).hexdigest()

# Solution to Part One of puzzle
found = False
number = 0

while not(found):
    hash = get_hash("".join([puzzle, str(number)]))

    found = hash.startswith("0"*5)
    
    if not found:
        number += 1

print(number)

# Solution to Part Two of puzzle
found = False
number = 0

while not(found):
    hash = get_hash("".join([puzzle, str(number)]))

    found = hash.startswith("0"*6)
    
    if not found:
        number += 1

print(number)