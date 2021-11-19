points = 0
playerOne = 0
playerTwo = 0

point = [0, 15, 30, 40]

playerOne = {
    "zero": 0,
    "fifteen": 15,
    "thirty": 30,
    "forty": 40,
    "name": "playerOne"
}

class Player:
    def __init__(self, score):
        self.score = score

    def setear_score(self, score):
        self.score = score

playerOneClass = Player(0)
playerTwoClass = Player(0)

def add_point(player, points_array, index):
    player.setear_score(points_array[index])


    def sumpoints():
        if playerOne == 0 and playerTwo == 0:
            print("PlayerOne {0} PlayerTwo {1}".format(playerOne, playerTwo))
        if playerOne == 30 and playerTwo == 15:
            print("PlayerOne {0} PlayerTwo {1}".format(playerOne, playerTwo))
        if playerOne == 40 and playerTwo == 40:
            print("Deuce")
        if playerOne == 41 and playerTwo == 40:
            print("Advantage PlayerOne")
        if playerOne == 40 and playerTwo == 41:
            print("Advantage PlayerTwo")
        if playerOne == 40 and playerTwo == 42:
            print("PlayerTwo wins")


if __name__ == '__main__':
    # INICIAR JUEGO
    add_point(playerOneClass, point, 1)
    print(playerOneClass.score)
