data = """<puzzle_input_goes_here>""".splitlines()

def part_one():
    count_of_increased_depth = 0

    prev = int(data.pop(0))
    loop = True

    while(loop):

        try:
            current = int(data.pop(0))
            sign = "+"
            if current > prev:
                count_of_increased_depth += 1
            else:
                sign = "-"
            
            print("%s -> %s = (%s)" % (prev, current, sign))
            
            prev = current
            
        except Exception as e:
            loop = False

    print("# of increased depth:", count_of_increased_depth)

def part_two():
    count_of_increased_depth = 0

    num_one = int(data.pop(0))
    num_two = int(data.pop(0))
    num_three = int(data.pop(0))

    prev = num_one + num_two + num_three

    loop = True

    while(loop):
        
        try:

            num_one = num_two
            num_two = num_three
            num_three = int(data.pop(0))
            
            current = num_one + num_two + num_three

            sign = "+"
            if current > prev:
                count_of_increased_depth += 1
            else:
                sign = "-"
            
            print("%s -> %s = (%s)" % (prev, current, sign))
            
            prev = current

        except Exception as e:
            loop = False

    print("# of increased depth:", count_of_increased_depth)


part_one()
part_two()