class Player():
    def __init__(self, score):
        self.score = score

    def setear_score(self, score):
        self.score = score

    def add_point(player, points_array, index):
        player.setear_score(points_array[index])
