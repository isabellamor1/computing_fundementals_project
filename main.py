import colorama
from colorama import Fore
from time import sleep
from Words import Words
from Words import LetterNumber as ln
from Leaderboard import Player
from Leaderboard import imput_player
from Leaderboard import display_boards
from Leaderboard import Leaderboard

colorama.init()

person = Player('name', 3, 3)
board3 = Leaderboard(3, person)
board4 = Leaderboard(4, person)
board5 = Leaderboard(5, person)
board6 = Leaderboard(6, person)
board7 = Leaderboard(7, person)


def instructions():
    """
    Prints out the game instructions
    :return: Instructions
    """
    print("\nInstructions:")
    print("\nFirst, choose how many letters you would like to be in your word by entering a number 3 to 7")
    sleep(1.5)
    print("\nNext, enter your first guess making sure to enter the correct number of letters")
    sleep(1.5)
    print("\nIf a letter in your guess is correct, the letter will turn green")
    sleep(1.5)
    ex_guess = "cat"
    ex_word = "pot"
    example = Words(ex_guess, ex_word)

    print("\nExample:")
    example.check_word()
    sleep(1.5)
    print(
        Fore.RESET + "\nIf a letter in your guess is also in the word but not in the correct spot, the letter will "
                     "turn yellow")
    sleep(1.5)
    print("\nExample:")
    ex_guess = 'tin'
    example = Words(ex_guess, ex_word)
    example.check_word()
    sleep(1.5)
    print("\nIf your guess is correct, a congratulatory message will appear")
    sleep(1.5)
    print(
        "\nIf you do not correctly guess the word in the number of guesses you are given, you lose and the word will "
        "be displayed")
    sleep(1.5)
    print("\nAfter you finish the game, you will have the option to play again")
    sleep(1.5)


loop = True

print("Welcome to the word guessing game")
p = input("Press 1 to play the game, 2 to view the instructions, or any other key to quit: ")

if p == '2':
    instructions()
    p = input(
        "\nWould you like to play a new game (press 1), view the leaderboard (press 2), or quit (press any other key): ")
    loop = True

if p == '1':
    loop = True

while loop:

    if p == '2':
        display_boards()
        p = input(
            "\nWould you like to play a new game (press 1), view the leaderboard (press 2), or quit (press any other "
            "key): ") 

    if p == '1':
        word_length = input("Please enter the number of letters you want in your word (3-7): ")
        num_class = ln(word_length)
        word = num_class.find_word()
        guesses = int(word_length) + 1
        words_guessed = 0
        for i in range(guesses):
            guess = ''
            if words_guessed == 0:
                guess = input('Please enter your first guess: ')
            elif words_guessed != 0:
                guess = input(Fore.RESET + "\n\nEnter your next guess: ")
            words_guessed += 1
            game = Words(guess, word)

            if game.spell_check(word_length):
                pass
            else:
                while not game.spell_check(word_length):
                    print('This word is not recognized by our systems')
                    guess = input('Please enter a new word: ')
                    game = Words(guess, word)
                    game.spell_check(word_length)

            if game.check_word():
                print("\nCongratulations, you guessed the word in", words_guessed, "guesses")
                name = input("Please enter your name:")
                plr = Player(name, int(word_length), int(words_guessed))
                imput_player(plr, int(word_length))
                break
            elif words_guessed == guesses:
                print(Fore.RESET + '\nSorry, you are out of guesses')
                print("The word was:", word)
                loop = True
            loop = True
        p = input(
            "\nWould you like to play a new game (press 1), view the leaderboard (press 2), or quit (press any other "
            "key): ") 
