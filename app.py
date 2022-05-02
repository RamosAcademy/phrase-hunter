# Import your Game class
from phrasehunter import Game, Phrase


# Create your Dunder Main statement.
if __name__ == "__main__":
    # Inside Dunder Main:
    # Create an instance of your Game class
    phrase = Phrase('Life is like a box of chocolates')
    print(phrase.phrase)

    # Start your game by calling the instance method that starts the game loop
