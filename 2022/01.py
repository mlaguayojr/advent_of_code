# --- Day 1: Calorie Counting ---

def load_data() -> dict:
    data = list()

    with open("./puzzle_input.txt") as f:
        data = f.readlines()

    for i in range(0, len(data)):
        data[i] = data[i].strip("\n")

    output = dict()
    elf_number = 1
    current_key = "elf%s" % (elf_number)
    output[current_key] = list()

    while(len(data) != 0):
        data_line = data.pop(0).strip("\n")

        if data_line != "":
            output[current_key].append(int(data_line))
        else:
            elf_number += 1
            current_key = "elf%s" % (elf_number)
            output[current_key] = list()

    return output

def part_one_solution():
    data = load_data()
    
    highest_calorie = 0

    for elf in data:
        total = sum(data[elf])
        if total > highest_calorie:
            highest_calorie = total

    print(highest_calorie)

def part_two_solution():
    data = load_data()

    for elf in data:
        data[elf] = sum(data[elf])
    
    calories = sorted(data.values(), reverse=True)
    calories = calories[:3]
    print(sum(calories))

if __name__=="__main__":
    # part_one_solution()
    # part_two_solution()