# Import your Game class
from phrasehunter import Game


# Create your Dunder Main statement.
if __name__ == "__main__":
    # Inside Dunder Main:
    # Create an instance of your Game class
    game = Game()
    print(game.active_phrase.phrase)
    game.active_phrase.display(game.guesses)
    # Start your game by calling the instance method that starts the game loop
