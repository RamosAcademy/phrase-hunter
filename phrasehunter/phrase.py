# Create your Phrase class logic here.


class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def display(self, guesses):
        '''Takes the `guesses` from the Game class so that it can compare the letters that have been guessed with the letters in the `phrase` attribute
        '''
        for letter in self.phrase:
            if guesses[0] == letter:
                print(f"{letter}", end=" ")
            else:
                print("_", end=" ")
