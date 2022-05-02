# Project 3: Phrase Hunters

## Step 1:

### Download project files

- [x] app.py will contain the main logic for your project -
- [x] another “phrasehunter” folder that contains game.py and phrase.py
- [x] **init**.py which allows you to ​import from a subdirectory https://youtu.be/cONc0NcKE7s
- [x] game.py will contain the Game class to manage the functioning of the game: it has methods for showing the game, handling interactions and checking for when the game is over
- [x] phrase.py will contain the Phrase class to manage individual phrases

## Step 2:

### Declare my classes

- [x] inside game.py, declare the Game class
- [x] inside phrase.py, declare the Phrase class

### Instantiate my classes.

- [x] Inside app.py, import my two classes
- [x] Add a dunder main inside my app.py
- [x] Create an instance of Phrase and assign it to a variable
- [x] Create an instance of Game and assign it to a variable.
      phrase = Phrase()
      game = Game()
- [x] test code: add temporary ​print​ statements to app.py to make sure the instances are being created.
      print(phrase)
      print(game)

## Step 3:

### Create the attributes and ​**init**​ methods for your classes

#### Game class parameters

- [x] The Game class ​**init**​ method has only s​elf ​as a parameter.

#### Game class attributes

- [x] missed​: Used to track the number of missed guesses by the player. The initial value is 0 since no guesses have been made at the start of the game.
- [x] phrases: ​A list of Phrase objects to use with the game. For now initialize the attribute to an empty list. In the next step you’ll work on initializing this property with a list of Phrase objects.
- [x] active_phrase​: This is the Phrase object that’s currently in play. The initial value is ​None
- [x] guesses: ​A list that contains all guesses made by the user during the course of the game. Start by setting it to a list that only contains a list with a string for a space. ​self.guesses = [“ “]

#### Phrase class parameters

- [x] The Phrase class **init** method should receive two parameters: ​self​ and ​phrase​.

#### Phrase class attributes

- [x] phrase​: This is the actual phrase as a string that the Phrase object is representing. This attribute should be set to the ​phrase​ parameter but converted to all lower case.

- [x] test code: Open up app.py and add the following code:
      phrase = Phrase('Life is like a box of chocolates')
      print(phrase.phrase)
