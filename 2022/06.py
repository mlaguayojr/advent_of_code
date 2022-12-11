# --- Day 6: Tuning Trouble ---

def load_puzzle() -> str:
    data = ""
    with open("./puzzle_input.txt") as f:
        data = f.readline()
    return data

def has_duplicate_characters(string :str) -> bool:
    chars = list(string)
    counts = dict()
    for i in chars:
        if i in counts.keys():
            counts[i] += 1
        else:
            counts[i] = 1
    
    return max(counts.values()) > 1

def find_marker(buffer :str, size :int = 4) -> tuple:
    sequence = None
    marker = 0

    for i in range(0, len(buffer)):
        stream = buffer[i:i+size]

        if not(has_duplicate_characters(stream)):
            sequence = stream
            marker = buffer.index(stream) + size
            break

    return (sequence, marker)

def part_one_solution():
    buffer = load_puzzle()
    print(find_marker(buffer))

def part_two_solution():
    buffer = load_puzzle()
    print(find_marker(buffer, 14))

part_one_solution()
part_two_solution()