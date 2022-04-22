
class player:

    def __init__(self, name, wordlength, num_guess):
        self.name = name
        self.wordlegth = wordlength
        self.num_guess = num_guess

    def display_player(self):
        print(self.name, "Number of guesses: ", self.num_guess)


class Leaderboard(player):

    players = []

    def __init__(self, wordlength, player):
        self.wordlength = wordlength
        self.player = player

    def add_player(self, player):
        players.append(self.player)

    def sort_players(self, players):


    def display_board(self):
        print(self.wordlength, "Letter Leaderboard:\n")
        for i in range(len(players)):
            print(i + 1,") ",self.name, "Number of guesses", self.num_guess)
