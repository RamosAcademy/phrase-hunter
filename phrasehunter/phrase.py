# Create your Phrase class logic here.


class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def display(self, guesses):
        '''Takes the `guesses` from the Game class so that it can compare the letters that have been guessed with the letters in the `phrase` attribute
        '''
        for letter in self.phrase:
            if letter in guesses:
                print(f"{letter}", end=" ")
            else:
                print("_", end=" ")

    def check_guess(self, guess):
        return True if guess in self.phrase else False

    def check_complete(self, guesses) -> bool:
        guesses_set = set(guesses)
        phrase_set = set(self.phrase)
        return True if phrase_set.issubset(guesses_set) else False
