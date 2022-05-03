class Player:
    

    def __init__(self, name, word_length, num_guess):
        self.name = name
        self.word_legth = word_length
        self.num_guess = num_guess

    def __str__(self):
        return f'Player({self.name}, {self.word_legth}, {self.num_guess})'

    def display_player(self):
        """
        Prints out the players name and number of guesses
        :return: Players name and number of guesses
        """
        print(self.name, "Number of guesses: ", self.num_guess)


class Leaderboard:
    

    def __init__(self, word_length, Player):
        self.word_length = word_length
        self.Player = Player
        self.Players = []

    def __str__(self):
        return f'(word_length:{self.word_length})'

    def add_player(self, Player):
        """
        Adds player to the leaderboard
        :param Player: object from class Player
        :return: self.Players
        """
        self.Players.append(Player)

    def sort_players(self):
        """
        Sorts the list of players
        :return: self.Players
        """
        self.Players.sort(key=lambda x: x.num_guess, reverse=False)

    def display_board(self):
        """
        Prints out the leaderboard
        :return: 
        """
        if len(self.Players) != 0:
            Leaderboard.sort_players(self)
            print('\nLeaderboard for', self.word_length, "Letter Words:\n")
            for i in range(len(self.Players)):
                self.Player = self.Players[i]
                print(i + 1, ") ", self.Player.name, "   |   Number of guesses:", self.Player.num_guess)


class TotalLeaderboard:

    def __init__(self, leaderboard, word_length):
        self.leaderboard = leaderboard
        self.word_length = word_length
        self.final_board = []
        self.Players = self.leaderboard.Players

    def __str__(self):
        return f'(word_length: {self.word_length})'

    def add_board(self, leaderboard):
        """
        Adds a leaderboard to the list of leaderboards
        :param leaderboard: Object from class Leaderboard
        :return: self.final_board
        """
        self.final_board.append(leaderboard)

    def display_total(self):
        """
        Prints out all the leaderboards in the list
        :return: 
        """
        for i in range(len(self.final_board)):
            self.leaderboard = self.final_board[i]
            Leaderboard.display_board(self.leaderboard)


person = Player('name', 3, 3)
board3 = Leaderboard(3, person)
board4 = Leaderboard(4, person)
board5 = Leaderboard(5, person)
board6 = Leaderboard(6, person)
board7 = Leaderboard(7, person)


def imput_player(Player, num):
    """
    Adds a player to a leaderboard corresponding to the number of letters in their word
    :param Player: object from class Player
    :param num: Length of the word
    :return: 
    """
    if num == 3:
        board3.add_player(Player)
    if num == 4:
        board4.add_player(Player)
    if num == 5:
        board5.add_player(Player)
    if num == 6:
        board6.add_player(Player)
    if num == 7:
        board7.add_player(Player)


totboard = TotalLeaderboard(board3, 3)
totboard.add_board(TotalLeaderboard(board3, 3))
totboard.add_board(TotalLeaderboard(board4, 4))
totboard.add_board(TotalLeaderboard(board5, 5))
totboard.add_board(TotalLeaderboard(board6, 6))
totboard.add_board(TotalLeaderboard(board7, 7))


def display_boards():
    """
    Displays all the boards
    :return: 
    """
    totboard.display_total()
