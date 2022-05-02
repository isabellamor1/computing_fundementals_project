import colorama
from colorama import Fore
from time import sleep
from Words import words
from Words import letter_number as ln
from Leaderboard import player
from Leaderboard import imput_player
from Leaderboard import display_boards

colorama.init()


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
    ex_word_letters = list(ex_word)
    print("\nExample:")
    words.check_word(ex_guess)
    sleep(1.5)
    print(
        Fore.RESET + "\nIf a letter in your guess is also in the word but not in the correct spot, the letter will "
                     "turn yellow")
    sleep(1.5)
    print("\nExample:")
    ex_guess = 'tin'
    words.check_word(ex_guess)
    sleep(1.5)
    print("\nIf your guess is correct, a congratulatory message will appear")
    sleep(1.5)
    print(
        "\nIf you do not correctly guess the word in the number of guesses you are given, you lose and the word will "
        "be displayed")
    sleep(1.5)
    print("\nAfter you finish the game, you will have the option to play again\n")
    sleep(1.5)


loop = True

print("Welcome to the word guessing game")
p = input("Press 1 to read the instructions, 2 to continue to the game, or any other key to quit: ")

if p != ('2' or '1' or '3'):
    loop = False

if p == '1':
    instructions()
    loop = True

while loop:

    if p == '2':
        wordlength = input("Please enter the number of letters you want in your word (3-7): ")
        num_class = ln(wordlength)
        word = num_class.find_word()
        word_letters = list(word)
        guesses = int(wordlength) + 1
        words_guessed = 0
        for i in range(guesses):
            guess = ''
            if words_guessed == 0:
                guess = input('Please enter your first guess: ')
            elif words_guessed != 0:
                guess = input(Fore.RESET + "\n\nEnter your next guess: ")
            words_guessed += 1
            game = words(guess, word)
            if game.check_word():
                print("\nCongratulations, you guessed the word in", words_guessed, "guesses")
                name = input("Please enter your name:")
                plr = player(name, wordlength, words_guessed)
                imput_player(plr, wordlength)
                break
            elif words_guessed == guesses:
                print(Fore.RESET + '\nSorry, you are out of guesses')
                print("The word was:", word)
                loop = True
            loop = True
    p = input("Would you like to play a new game (press 1), view the leaderboard (press 2), or quit (press 3): ")

    if p == '2':
        display_boards()
        p = input("Would you like to play a new game (press 1), view the leaderboard (press 2), or quit (press 3): ")
        loop = True

    else:
        while p != ('1' or '2' or '3'):
            print("Please enter 1, 2, or 3")
            p = input(
                "Would you like to play a new game (press 1), view the leaderboard (press 2), or quit (press 3): ")
