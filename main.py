import random
import colorama
from colorama import Fore
from time import sleep
import Words
from Words import words
from Words import letter

colorama.init()


def find_word(num):
    """
    Returns a randomly generated word with given correct number of letters
    :param num: number of letters
    :return: word
    """
    if num == '3':
        print("\nYou have 4 guesses")
        with open("three.txt", "r") as wordfile:
            all_words = wordfile.read()
            all_words.lower()
            words = all_words.split()
            word_num = random.randint(0, len(words))
            fin_word = words[word_num]
            return fin_word.lower()
    if num == '4':
        print("\nYou have 5 guesses")
        with open("four.txt", "r") as wordfile:
            all_words = wordfile.read()
            words = all_words.split()
            word_num = random.randint(0, len(words))
            fin_word = words[word_num]
            return fin_word
    if num == '5':
        print("\nYou have 6 guesses")
        with open("five.txt", "r") as wordfile:
            all_words = wordfile.read()
            words = all_words.split()
            word_num = random.randint(0, len(words))
            fin_word = words[word_num]
            return fin_word
    if num == '6':
        print("\nYou have 7 guesses")
        with open("six.txt", "r") as wordfile:
            all_words = wordfile.read()
            words = all_words.split()
            word_num = random.randint(0, len(words))
            fin_word = words[word_num]
            return fin_word
    if num == '7':
        print("\nYou have 8 guesses")
        with open("seven.txt", "r") as wordfile:
            all_words = wordfile.read()
            words = all_words.split()
            word_num = random.randint(0, len(words))
            fin_word = words[word_num]
            return fin_word


# def turn_green(letter):
#     """
#     Turns a given letter green and prints it
#     :param letter: non-green letter
#     :return: printed green letter
#     """
#     print(Fore.GREEN + letter, end="")
#
#
# def turn_yellow(letter):
#     """
#     Turns a given letter yellow and prints it
#     :param letter: non-yellow letter
#     :return: printed yellow letter
#     """
#     print(Fore.YELLOW + letter, end="")
#

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


# def check_word(user_guess, genword_letters):
    # """
    # Returns the users guess with the letter colors changed depending on their placement in the generated word
    # :param user_guess: Players guess
    # :param genword_letters: Generated word split into individual letters
    # :return: Players guess with the letters their corresponding colors
    # """
    #
    # guess_letters = list(user_guess)
    # while len(guess_letters) != len(genword_letters):
    #     user_guess = input("Please enter the correct number of letters: ")
    #     guess_letters = list(user_guess)
    # if guess_letters == genword_letters:
    #     return True
    # else:
    #     for j in range(len(guess_letters)):
    #         if guess_letters[j] in genword_letters and guess_letters[j] != genword_letters[j]:
    #             turn_yellow(guess_letters[j])
    #         if guess_letters[j] == genword_letters[j]:
    #             turn_green(guess_letters[j])
    #         elif guess_letters[j] not in genword_letters:
    #             print(Fore.RESET + guess_letters[j], end="")
    # return False


loop = True

print("Welcome to the word guessing game")
n = input("Press 1 to read the instructions, press 2 to continue to the game, press any other key to quit: ")

if n != ('2' or '1'):
    loop = False

if n == '1':
    instructions()
    loop = True

while loop:
    p = input("Would you like to play a new game (press 1), view the leaderboard (press 2), or quit (press 3): ")
    if p == '1':
        letters = input("Please enter the number of letters you want in your word (3-7): ")
        word = find_word(letters)
        word_letters = list(word)
        guesses = int(letters) + 1
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
                name = input("Please enter your name")

                break
            elif words_guessed == guesses:
                print(Fore.RESET + '\nSorry, you are out of guesses')
                print("The word was:", word)
                loop = True
            loop = True

    #if p == '2':


    if p == '3':
        break
    if p != ('1' or '2' or '3'):
        print("Please enter 1 or 2")
