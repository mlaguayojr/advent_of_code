data = """<puzzle_input_goes_here>""".splitlines()

def part_one():
    horizontal_pos = 0
    depth = 0
    loop = True
    
    while(loop):
        try:
            [direction, amount] = (data.pop(0)).split(" ")
            print(direction, amount)
            amount = int(amount)
            
            if direction == "down":
                depth += amount
            elif direction == "up":
                depth -= amount
            elif direction == "forward":
                horizontal_pos += amount
            else:
                print("unknown direction \"%s\"" % (direction))
                
        except Exception as e:
            print("error:", e)
            loop = False
            
    print("Horizontal: %s, Depth: %s, Answer: %s" % (horizontal_pos, depth, horizontal_pos * depth))

def part_two():
    horizontal_pos = 0
    depth = 0
    aim = 0
    
    loop = True
    
    while(loop):
        try:
            [direction, amount] = (data.pop(0)).split(" ")
            print(direction, amount)
            amount = int(amount)
            
            #print("Before:", horizontal_pos, depth, aim)
            
            if direction == "down":
                aim += amount
            elif direction == "up":
                aim -= amount
            elif direction == "forward":
                horizontal_pos += amount
                depth += (aim * amount)
            else:
                print("unknown direction \"%s\"" % (direction))
            
            #print("After:", horizontal_pos, depth, aim)
        except Exception as e:
            print("error:", e)
            loop = False
            
    print("Horizontal: %s, Depth: %s, Aim: %s, Answer: %s" % (horizontal_pos, depth, aim, horizontal_pos * depth))

part_one()
part_two()