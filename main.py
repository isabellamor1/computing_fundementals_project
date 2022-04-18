import random
import colorama
from colorama import Fore
import leaderboard

colorama.init()


def find_word(num):
    if num == '3':
        with open("three.txt", "r") as wordfile:
            all_words = wordfile.read()
            all_words.lower()
            words = all_words.split()
            word_num = random.randint(0, len(words))
            word = words[word_num]
            return word.lower()
    if num == '4':
        with open("four.txt", "r") as wordfile:
            all_words = wordfile.read()
            words = all_words.split()
            word_num = random.randint(0, len(words))
            word = words[word_num]
            return word
    if num == '5':
        with open("five.txt", "r") as wordfile:
            all_words = wordfile.read()
            words = all_words.split()
            word_num = random.randint(0, len(words))
            word = words[word_num]
            return word
    if num == '6':
        with open("six.txt", "r") as wordfile:
            all_words = wordfile.read()
            words = all_words.split()
            word_num = random.randint(0, len(words))
            word = words[word_num]
            return word
    if num == '7':
        with open("seven.txt", "r") as wordfile:
            all_words = wordfile.read()
            words = all_words.split()
            word_num = random.randint(0, len(words))
            word = words[word_num]
            return word


def turn_green(letter):
    print(Fore.GREEN + letter)


def turn_yellow(letter):
    print(Fore.YELLOW + letter)



def check_word(guess, word_letters):
    guess_letters = list(guess)
    if guess_letters == word_letters:
        return True
    else:
        for i in range(len(guess_letters)):
            if guess_letters[i] in word_letters and guess_letters[i] != word_letters[i]:
                turn_yellow(guess_letters[i])
            if guess_letters[i] == word_letters[i]:
                turn_green(guess_letters[i])
            elif guess_letters[i] not in word_letters:
                print(Fore.RESET +guess_letters[i])
    return False

# def show_leaderboard():


loop = True
while loop:
    p = input("Would you like to play a new game (press 1) or view the leaderboard (press 2): ")
    if p == '1':
        letters = input("Please enter the number of letters you want in your word (3-7)")
        word = find_word(letters)
        word_letters = list(word)
        guesses = int(letters) + 1
        words_guessed = 0
        for i in range(guesses):
            guess = ''
            if words_guessed == 0:
                guess = input('Please enter your first guess: ')
            elif words_guessed != 0:
                guess = input(Fore.RESET + "Enter your guess: ")
            words_guessed += 1
            if check_word(guess, word_letters):
                print("Congratulations, you guessed the word in", words_guessed, "guesses")
                break
            elif words_guessed == guesses:
                print(Fore.RESET + 'Sorry, you are out of guesses')
                print("The word was:",word)
    loop = True

    # if p == 2:
    #     show_leaderboard()

    if p != 1 or 2:
        loop = False
