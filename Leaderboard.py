
class player:

    def __init__(self, name, wordlength, num_guess):
        self.name = name
        self.wordlegth = wordlength
        self.num_guess = num_guess

    def __str__(self):
        return f'player({self.name}, {self.wordlegth}, {self.num_guess})'

    def display_player(self):
        print(self.name, "Number of guesses: ", self.num_guess)


class Leaderboard:


    def __init__(self, wordlength, player):
        self.wordlength = wordlength
        self.player = player
        self.players = []

    def __str__(self):
        return f'(wordlength:{self.wordlength})'

    def add_player(self, player):
        self.players.append(player)

    def takenumguess(self, player):
        return player.num_guess

    def sort_players(self, players):
        sorted_list = sorted(players, key=self.takenumguess)
        return sorted_list

    def display_board(self):
        print('\nLeaderboard for', self.wordlength, "Letter Words:\n")
        for i in range(len(self.players)):
            self.player = self.players[i]
            print(i + 1,") ",self.player.name, "   |   Number of guesses:", self.player.num_guess)

class TotalLeaderboard:


    def __init__(self,leaderboard, wordlength):
        self.leaderboard = leaderboard
        self.wordlength = wordlength
        self.final_board = []
        self.players = self.leaderboard.players

    def __str__(self):
        return f'(wordlength: {self.wordlength})'


    def add_board(self, leaderboard):
        self.final_board.append(leaderboard)
        #sort so boards are in ascending order

    def display_total(self):
        for i in range(len(self.final_board)):
            self.leaderboard = self.final_board[i]
            print(i)
            Leaderboard.display_board(self.leaderboard)

person = player('name', 3, 3)
board3 = Leaderboard(3,person)
board4 = Leaderboard(4,person)
board5 = Leaderboard(5,person)
board6 = Leaderboard(6,person)
board7 = Leaderboard(7,person)

def imput_player(player,num):
    if num == 3:
        board3.add_player(player)
    if num == 4:
        board4.add_player(player)
    if num == 5:
        board5.add_player(player)
    if num == 6:
        board6.add_player(player)
    if num == 7:
        board7.add_player(player)

