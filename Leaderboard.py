
class player:

    def __init__(self, name, wordlength, num_guess):
        self.name = name
        self.wordlegth = wordlength
        self.num_guess = num_guess

    def display_player(self):
        print(self.name, "Number of guesses: ", self.num_guess)


class Leaderboard:


    def __init__(self, wordlength, player):
        self.wordlength = wordlength
        self.player = player
        self.players = []

    def add_player(self):
        self.players.append(self.player)

    def takenumguess(self, player):
        return player.num_guess

    def sort_players(self, players):
        sorted_list = sorted(players, key=self.takenumguess)
        return sorted_list

    def display_board(self):
        print(self.wordlength, "Letter Words:\n")
        for i in range(len(self.players)):
            print(i + 1,") ",self.player.name, "Number of guesses", self.player.num_guess)

class TotalLeaderboard:


    def __init__(self,leaderboard, wordlength):
        self.leaderboard = leaderboard
        self.wordlength = wordlength
        self.final_board = []

    def add_board(self):
        self.final_board.append(self.leaderboard)
        #sort so boards are in ascending order

    def display_total(self):
        print("Leaderboard:")
        for i in range(len(self.final_board)):
            Leaderboard.display_board()
