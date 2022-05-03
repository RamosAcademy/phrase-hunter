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
            Phrase('Honey Where is my super-suit'),
            Phrase('The Matrix has you Neo'),
        ]
        self.active_phrase = self.get_random_phrase()
        self.guesses = [" "]

    def welcome(self):
        print("\n", "\n", "      ", "="*50, "\n", "\n",
              "        Hello Beautiful Human! Let's play Phrase Hunter.", "\n", "\n", "      ", "="*50, "\n\n\n", "Number missed: ", self.missed, "\n\n", "_ "*8, "\n\n")

    def get_random_phrase(self):
        ''' Select and then return a random phrase from the array of phrases stored in the Game class ​phrase​ property
        '''
        self.rando = randint(0, 4)
        return self.phrases[self.rando]
