import itertools

class City:

    def __init__(self, name :str):
        self.name = name
        self.paths = dict()

    def add_route(self, city_name :str, distance :int):
        if not(city_name in self.paths.keys()):
            self.paths[city_name] = distance


class Instruction:

    def __init__(self, line :str):
        (CityA, _, CityB, _, Distance) = line.split(" ")
        self.do = (CityA, CityB, int(Distance) )


if __name__=="__main__":

    # Get data
    data = []

    with open("puzzle_input.txt") as f:
        data = f.readlines()

    # Build maps
    cities = {}

    for i in data:
        (city1_name, city2_name, distance) = Instruction(i.rstrip()).do

        for x in [city1_name, city2_name]:

            if not(x in cities.keys()):
                cities[x] = City(x)

        city_1 = cities[city1_name]
        city_1.add_route(city2_name, distance)

        city_2 = cities[city2_name]
        city_2.add_route(city1_name, distance)


    city_permutations = list(itertools.permutations(cities.keys()))

    def part_one_solution():

        min_distance = None
        distance_history = {}

        for route in city_permutations:

            distance = 0

            for index in range(0, len(route)-1):
                city_name = route[index]
                next_city = route[index+1]

                distance += cities[city_name].paths[next_city]
            
            distance_history[distance] = route

            if (min_distance is None) or (distance < min_distance):
                min_distance = distance

        print(min_distance, ":", distance_history[min_distance])

    def part_two_solution():
        max_distance = None
        distance_history = {}

        for route in city_permutations:

            distance = 0

            for index in range(0, len(route)-1):
                city_name = route[index]
                next_city = route[index+1]

                distance += cities[city_name].paths[next_city]
            
            distance_history[distance] = route

            if (max_distance is None) or (distance > max_distance):
                max_distance = distance

        print(max_distance, ":", distance_history[max_distance])

    part_one_solution()
    part_two_solution()