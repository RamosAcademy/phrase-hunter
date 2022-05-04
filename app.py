# Import your Game class
from cv2 import phase
from phrasehunter import Game


# Create your Dunder Main statement.
if __name__ == "__main__":
    # Inside Dunder Main:
    # Create an instance of your Game class
    game = Game()
    print(game.active_phrase.phrase)
    game.start()
    # Start your game by calling the instance method that starts the game loop
