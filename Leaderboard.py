
class player:

    def __init__(self, name, wordlength, num_guess):
        self.name = name
        self.wordlegth = wordlength
        self.num_guess = num_guess

    def display_player(self):
        print(self.name, "Number of guesses: ", self.num_guess)


class Leaderboard(player):

    players = []

    def __init__(self, wordlength, player, name, num_guess):
        super.__init__(name, num_guess)
        self.wordlength = wordlength
        self.player = player

    def add_player(self, player):
        players.append(self.player)

    def sort_players(self, players):


    def display_board(self):
        print(self.wordlength, "Letter Words:\n")
        for i in range(len(players)):
            print(i + 1,") ",self.name, "Number of guesses", self.num_guess)

class total_leaderboard(Leaderboard(player)):

    final_board = []

    def __init__(self,Leaderboard, wordlength, player, name, num_guess):
        super.__init__(wordlength, player, name, num_guess)
        self.leaderboard = Leaderboard

    def add_board(self, leaderboard):
        final_board.append(self.leaderboard)
        #sort so boards are in ascending order

    def display_total(self):
        print("Leaderboard:")
        for i in range(len(final_board)):
            Leaderboard.display_board()
