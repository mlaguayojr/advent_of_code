def load_puzzle() -> list:
    data = list()
    
    with open("./puzzle_input.txt") as f:
        data = f.readlines()
    
    return data

def get_directions(data) -> list:
    directions = list()
    for i in data:
        if "move" in i:
            [_, number_of_containers, _, from_column, _, to_column] = i.strip().split(" ")
            directions.append([ int(x) for x in [number_of_containers, from_column, to_column] ])

    return directions

def get_containers(data) -> dict:
    stack_data = list()

    for i in data:
        if not ("move" in i) and (i.strip() != ""):
            stack_data.append(i.strip("\n"))
    
    stacks = dict()

    for x in stack_data[-1].split(" "):
        if x != "":
            stacks[int(x)] = list()

    for line in stack_data[:-1]:
        containers = list()
        for i in range(0, len(line), 4):
            containers.append(line[i:i+4].strip())

        for i in range(0, len(containers)):
            if containers[i] != "":
                stacks[i+1].append(list(containers[i])[1])

    for i in stacks.keys():
        stacks[i].reverse()

    return stacks

def move_container(containers :dict, direction :list, keep_order = False) -> dict:
    [number_of_containers, from_column, to_column] = direction
    
    if not(keep_order):
        while number_of_containers != 0:
            try:
                container = containers[from_column].pop()
                containers[to_column].append(container)
            except Exception as e:
                pass
            number_of_containers -= 1
    else:
        move_containers = list()
        while number_of_containers != 0:
            try:
                move_containers.append(containers[from_column].pop())
            except Exception as e:
                pass
            number_of_containers -= 1

        move_containers.reverse()
        containers[to_column].extend(move_containers)

    return containers

def part_one_solution():
    data = load_puzzle()
    stack_data = get_containers(data)
    directions = get_directions(data)

    for direction in directions:
        stack_data = move_container(stack_data, direction)

    answer = ""
    for i in stack_data.keys():
        answer += stack_data[i][-1]

    print(answer)

def part_two_solution():
    data = load_puzzle()
    stack_data = get_containers(data)
    directions = get_directions(data)

    for direction in directions:
        stack_data = move_container(stack_data, direction, True)

    answer = ""
    for i in stack_data.keys():
        answer += stack_data[i][-1]

    print(answer)

part_one_solution()
part_two_solution()