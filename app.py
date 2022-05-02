# Import your Game class
from phrasehunter import Game, Phrase


# Create your Dunder Main statement.
if __name__ == "__main__":
    # Inside Dunder Main:
    # Create an instance of your Game class
    phrase = Phrase()
    game = Game()

    print(phrase)
    print(game)

    # Start your game by calling the instance method that starts the game loop
