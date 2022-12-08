# --- Day 2: Rock Paper Scissors ---
def load_data() -> list:
    """Load puzzle input from file"""
    data = list()

    with open("./puzzle_input.txt") as f:
        data = f.readlines()
    
    output = list()
    for i in data:
        output.append(i.strip().split(" "))

    return output

def decipher_hand(opponent_play :str, my_play :str) -> str:
    opponent_play = translate_hand(opponent_play)

    results = {
        "X": {
            "Rock": "Scissors",
            "Paper": "Rock",
            "Scissors": "Paper"
        },
        "Z": {
            "Rock": "Paper",
            "Paper": "Scissors",
            "Scissors": "Rock"
        },
        "Y": {
            opponent_play: opponent_play
        }
    }

    return results[my_play][opponent_play]

def translate_hand(character :str) -> str:
    choices = {
        "A": "Rock",
        "X": "Rock",
        "B": "Paper",
        "Y": "Paper",
        "C": "Scissors",
        "Z": "Scissors",
    }

    return choices[character]

def winning_hand(opponent_play :str, my_hand :str) -> str:
    if opponent_play == "Rock":
        if my_hand == "Paper":
            return "won"
        elif my_hand == "Scissors":
            return "lost"
        else:
            return "tie"

    if opponent_play == "Paper":
        if my_hand == "Paper":
            return "tie"
        elif my_hand == "Scissors":
            return "won"
        else:
            return "lost"

    if opponent_play == "Scissors":
        if my_hand == "Paper":
            return "lost"
        elif my_hand == "Scissors":
            return "tie"
        else:
            return "won"

def round_point(round_result :str, my_hand :str) -> int:
    round_point = {
        "won": 6,
        "tie": 3,
        "lost": 0
    }

    hand_point = {
        "Rock": 1,
        "Paper": 2,
        "Scissors": 3
    }

    return round_point[round_result] + hand_point[my_hand]

def part_one_solution():
    data = load_data()
    total_points = 0

    for [opponent_play, my_play] in data:
        opponent_play = translate_hand(opponent_play)
        my_play = translate_hand(my_play)
        print("Opponent:", opponent_play, "Me:", my_play)
        round_result = winning_hand(opponent_play, my_play)
        print("Result:", round_result)
        total_points += round_point(round_result, my_play)

    print("Total points:", total_points)


def part_two_solution():
    data = load_data()
    total_points = 0

    for [opponent_play, my_play] in data:
        my_play = decipher_hand(opponent_play, my_play)
        opponent_play = translate_hand(opponent_play)
        print("Opponent:", opponent_play, "Me:", my_play)
        round_result = winning_hand(opponent_play, my_play)
        print("Result:", round_result)
        total_points += round_point(round_result, my_play)

    print("Total points:", total_points)

if __name__=="__main__":
    # part_one_solution()
    # part_two_solution()