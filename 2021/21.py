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
    die = DerterministicDie() # Create the Die to use

    players = [
        Player("Player 1", 4, 10, 1, 1000),
        Player("Player 2", 8, 10, 1, 1000)
    ]

    player = players.pop(0)

    loop = True
    while loop:
        others = players
        print("before rolls:", player)

        for i in range(0, 3):
            move = die.Roll()
            while move != 0:
                player.MovePawn()
                move -= 1
        
        player.AddPoints(player.GetPosition())

        print("after rolls:", player)

        if player.Winner():
            loop = False
        else:
            players.append(player)
            player = players.pop(0)

    for remaining_player in others:
        print(remaining_player, die.rollCount, (remaining_player.points * die.rollCount))

part_one()