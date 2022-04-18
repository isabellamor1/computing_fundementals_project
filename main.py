import random
import colorama
from colorama import Fore

colorama.init()


def find_word(num):
    if num == 3:
        with open("three.txt", "r") as wordfile:
            all_words = wordfile.read()
            words = all_words.split
            word_num = random.randint(0, len(all_words))
            word = words[word_num]
            return word
    if num == 4:
        with open("four.txt", "r") as wordfile:
            all_words = wordfile.read()
            words = all_words.split
            word_num = random.randint(0, len(all_words))
            word = words[word_num]
            return word
    if num == 5:
        with open("five.txt", "r") as wordfile:
            all_words = wordfile.read()
            words = all_words.split
            word_num = random.randint(0, len(all_words))
            word = words[word_num]
            return word
    if num == 6:
        with open("six.txt", "r") as wordfile:
            all_words = wordfile.read()
            words = all_words.split
            word_num = random.randint(0, len(all_words))
            word = words[word_num]
            return word
    if num == 7:
        with open("seven.txt", "r") as wordfile:
            all_words = wordfile.read()
            words = all_words.split
            word_num = random.randint(0, len(all_words))
            word = words[word_num]
            return word


def turn_green(letter):
    print(Fore.GREEN + letter)


def turn_yellow(letter):
    print(Fore.YELLOW + letter)


def check_word(guess):
    guess_letters = guess.split
    for i in range(guess_letters):
        if guess_letters == word_letters:
            return True
        elif guess_letters[i] in word_letters:
            turn_yellow(guess_letters[i])

        elif guess_letters[i] == word_letters[i]:
            turn_green(guess_letters[i])
        elif guess_letters[i] not in word_letters:
            print(guess_letters[i])


# def show_leaderboard():


loop = True
while loop:
    p = input(print("Would you like to play a new game (press 1) or view the leaderboard (press 2): "))
    if p == 1:
        letters = input("Please enter the number of letters you want in your word (3-7)")
        word = find_word(letters)
        word_letters = word.split
        guesses = int(letters) + 1
        words_guessed = 0
        for i in range(guesses):
            if words_guessed == 0:
                guess = input('Please enter your first guess: ')
            if words_guessed != 0:
                guess = input("Enter your guess: ")
            words_guessed += 1
            if check_word(guess) == True:
                print("Congradulations, you guesses the word in ", words_guessed, "guesses")
            elif words_guessed == guesses:
                print('Sorry, you are out of guesses')
    
    if p != 1 or 2:
        loop = False
