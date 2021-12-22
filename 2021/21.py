class DerterministicDie:
    def __init__(self) -> None:
        self.value = 0
        self.rollCount = 0

    def Roll(self) -> int:
        self.rollCount += 1
        if self.value < 100:
            self.value += 1
        else:
            self.value = 1
        return self.value

    def __str__(self) -> str:
        return "roll #%s was %s" % (self.rollCount, self.value)

class Player:
    def __init__(self, name :str, positition :int, position_max :int, position_min :int, max_points :int) -> None:
        self.position = positition
        self.max_pos = position_max
        self.min_pos = position_min
        self.name = name
        self.points = 0
        self.max_points = max_points

    def GetPosition(self) -> int:
        return self.position

    def MovePawn(self):
        if self.position < self.max_pos:
            self.position += 1
        else:
            self.position = self.min_pos

    def AddPoints(self, points :int):
        self.points += points

    def Winner(self) -> bool:
        return (self.points >= self.max_points)

    def __str__(self) -> str:
        return "%s currently has %s points" % (self.name, self.points)

def part_one():
    # Solution for Part One

    # Create Die
    die = DerterministicDie()

    # Create list of Players
    players = [
        Player("Player 1", 4, 10, 1, 1000), # Example data for Player 1
        Player("Player 2", 8, 10, 1, 1000)  # Example data for Player 2
    ]

    # Get first Player object from players list (e.g., "Player 1" since "Player 1" was added first.)
    player = players.pop(0)

    loop = True
    while loop:
        others = players
        print("before rolls:", player) # Debug for progress before player starts their respective rolls

        for i in range(0, 3):
            move = die.Roll()
            while move != 0:
                player.MovePawn()
                move -= 1
        
        player.AddPoints(player.GetPosition())

        print("after rolls:", player) # Debug for progress before player ends their turn

        if player.Winner(): # Check if player is winning now
            loop = False
        else:
            players.append(player)
            player = players.pop(0)

    # Iterate through remaining players (e.g., "Player 2", etc.)
    for remaining_player in others:
        print(remaining_player, die.rollCount, (remaining_player.points * die.rollCount)) # Debug for player name, how many times the die has been rolled, and expected answer

part_one()