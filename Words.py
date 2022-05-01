import random
import colorama
from colorama import Fore


class words:

    def __init__(self, guess, word):
        self.guess = guess
        self.word = word

    def check_word(self):
        """
        Returns the users guess with the letter colors changed depending on their placement in the generated word
        :return: Players guess with the letters their corresponding colors
        """

        guess_letters = list(self.guess)
        genword_letters = list(self.word)
        while len(guess_letters) != len(genword_letters):
            self.guess = input("Please enter the correct number of letters: ")
            guess_letters = list(self.guess)
        if guess_letters == genword_letters:
            return True
        else:
            for j in range(len(guess_letters)):
                if guess_letters[j] in genword_letters and guess_letters[j] != genword_letters[j]:
                    letter.turn_yellow(guess_letters[j])
                if guess_letters[j] == genword_letters[j]:
                    letter.turn_green(guess_letters[j])
                elif guess_letters[j] not in genword_letters:
                    print(Fore.RESET + guess_letters[j], end="")
        return False


class letter:

    def __init__(self, letter):
        self.letter = letter

    def turn_green(self):
        """
        Turns a given letter green and prints it
        :return: printed green letter
        """
        print(Fore.GREEN + self.letter, end="")

    def turn_yellow(self):
        """
        Turns a given letter yellow and prints it
        :return: printed yellow letter
        """
        print(Fore.YELLOW + self.letter, end="")


class letter_number:

    def __init__(self, num):
        self.num = num

    def find_word(self):
        """
        Returns a randomly generated word with given correct number of letters
        :param num: number of letters
        :return: word
        """
        if self.num == '3':
            print("\nYou have 4 guesses")
            with open("three.txt", "r") as wordfile:
                all_words = wordfile.read()
                all_words.lower()
                words = all_words.split()
                word_num = random.randint(0, len(words))
                fin_word = words[word_num]
                return fin_word.lower()
        if self.num == '4':
            print("\nYou have 5 guesses")
            with open("four.txt", "r") as wordfile:
                all_words = wordfile.read()
                words = all_words.split()
                word_num = random.randint(0, len(words))
                fin_word = words[word_num]
                return fin_word
        if self.num == '5':
            print("\nYou have 6 guesses")
            with open("five.txt", "r") as wordfile:
                all_words = wordfile.read()
                words = all_words.split()
                word_num = random.randint(0, len(words))
                fin_word = words[word_num]
                return fin_word
        if self.num == '6':
            print("\nYou have 7 guesses")
            with open("six.txt", "r") as wordfile:
                all_words = wordfile.read()
                words = all_words.split()
                word_num = random.randint(0, len(words))
                fin_word = words[word_num]
                return fin_word
        if self.num == '7':
            print("\nYou have 8 guesses")
            with open("seven.txt", "r") as wordfile:
                all_words = wordfile.read()
                words = all_words.split()
                word_num = random.randint(0, len(words))
                fin_word = words[word_num]
                return fin_word