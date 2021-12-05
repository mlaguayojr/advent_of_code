# Load Puzzle inputs from file
input = []
with open("2021\\03_sample.txt", "r") as f:
    input = f.readlines()

for element in range(0, len(input)):
    input[element] = input[element].strip()

def toDecimal(_list):
    "Convert binary value to decimal number"
    value = 0
    size_of_data = len(_list)

    for i in range(size_of_data-1, -1, -1):
        #print(i, _list[i], pow(2, i))
        if int(_list[i]) == 1:
            value += pow(2, size_of_data - 1 - i)

    return value

def invert(_list):
    "Flip binary value elements"
    value = _list
    
    for i in range(0, len(value)):
        if value[i] == 1:
            value[i] = 0
        else:
            value[i] = 1

    return value

def part_one():
    "Solution to part one"
    gamma_rate = [0]*len(input[0])

    bit_index = 0
    
    while bit_index < len(gamma_rate):

        num_ones = 0
        num_zeros = 0
    
        for entries in input:

            if int(entries[bit_index]) == 1:
                num_ones += 1
            else:
                num_zeros += 1
            
        if num_ones > num_zeros:
            gamma_rate[bit_index] = 1

        bit_index += 1
    
    a = toDecimal(gamma_rate)
    b = toDecimal(invert(gamma_rate))
    print(a * b)

def filter(_list, index, value):
    keep = []

    for i in _list:
        if int(i[index]) == value:
            keep.append(i)

    return keep

def part_two():
    "Solution to part two"
    oxygen_values = input
    co2_values = input
    bit_index = 0

    while len(oxygen_values) > 1:

        num_ones = 0
        num_zeros = 0

        for values in oxygen_values:

            if int(values[bit_index]) == 1:
                num_ones += 1
            else:
                num_zeros += 1

        if num_ones >= num_zeros:
            oxygen_values = filter(oxygen_values, bit_index, 1)
        else:
            oxygen_values = filter(oxygen_values, bit_index, 0)

        bit_index += 1

    oxygen_values = list(oxygen_values[0])
    print(oxygen_values)

    bit_index = 0

    while len(co2_values) > 1:

        num_ones = 0
        num_zeros = 0

        for values in co2_values:

            if int(values[bit_index]) == 1:
                num_ones += 1
            else:
                num_zeros += 1

        if num_zeros <= num_ones:
            co2_values = filter(co2_values, bit_index, 0)
        else:
            co2_values = filter(co2_values, bit_index, 1)

        bit_index += 1

    co2_values = list(co2_values[0])
    print(co2_values)

    a = toDecimal(oxygen_values)
    b = toDecimal(co2_values)
    print(a * b)

#part_one()
part_two()