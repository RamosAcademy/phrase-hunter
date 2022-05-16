from phrasehunter.phrase import Phrase
from random import randint
# Create your Game class logic in here.


class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = [
            Phrase('Life is like a box of chocolates'),
            Phrase('There is no trying'),
            Phrase('Hello Beautiful world'),
            Phrase('Honey Where is my super suit'),
            Phrase('The Matrix has you Neo'),
        ]
        self.active_phrase = self.get_random_phrase()
        self.guesses = [" "]

    def get_random_phrase(self):
        ''' Select and then return a random phrase from the array of phrases stored in the Game class ​phrase​ property
        '''
        self.rando = randint(0, 4)
        return self.phrases[self.rando]

    def welcome(self):
        print("\n", "\n", "      ", "="*50, "\n", "\n",
              "        Hello Beautiful Human! Let's play Phrase Hunter.", "\n", "\n", "      ", "="*50, "\n\n\n")

    def get_guess(self):
        return input("\n\nEnter a letter: ")

    def game_over(self):
        if self.missed == 5:
            print("Better luck next time, friend!")
        else:
            print(f"\nWoohoo! Congrats You Won!\n")

    def start(self):
        self.welcome()
        complete = False
        while self.missed < 5 and not complete:
            print("Number missed: ", self.missed, "\n\n")
            self.active_phrase.display(self.guesses)
            user_guess = self.get_guess()
            self.guesses.append(user_guess)
            if not self.active_phrase.check_guess(user_guess):
                self.missed += 1
            complete = self.active_phrase.check_complete(self.guesses)
        self.game_over()
