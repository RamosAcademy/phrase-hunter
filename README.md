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

## Step 4:

### Time to create your phrases that the game will randomly choose from when showing a new phrase to the player.

- [x] You will need to import your Phrase class into the Game class.

#### There are multiple ways to create your phrases and add them to the Game class’s ​phrases ​property:

- [] Option #1: Inside the Game class, create a method called ​create_phrases()​ that creates and returns a list of five new​ Phrase ​objects, and then set the ​phrases property to call that method​.
- [x] Option #2: Simply add 5 new Phrase objects directly in the empty array that was originally set as the value of the​ phrases​ property.

#### Don’t forget to pass in the actual string phrase that the Phrase object is representing.

- [x] A string phrase should only include letters and spaces -- no numbers, punctuation or other special characters.
- [x] A phrase must contain more than one word.

- [x] Test code: Open up the app.py file and add the following code (note that you don’t need to import Phrase in app.py anymore):
      game = Game()
      for phrase in game.phrases:
      print(phrase.phrase)

## Step 5:

### Write the get_random_phrase() method mentioned in the last step.

- [x] This method goes inside the Game class in the game.py file.
- [x] This method should select and then return a random phrase from the array of phrases stored in the Game class’s ​phrase​ property.
- [x] You will need to import random​.

- [x] Test code: Open up the app.py file and add the following code:
      def print_phrase(phrase_object)
      print(f”The phrase is: {phrase_object.phrase}”)
      game = Game()
      print_phrase(game.get_random_phrase())
      print_phrase(game.get_random_phrase())
      print_phrase(game.get_random_phrase())
      print_phrase(game.get_random_phrase())
      print_phrase(game.get_random_phrase())

## Step 6:

- [x] Go back to the `__init__` of your Game class and change the `self.active_phrase` to be the result of calling the `get_random_phrase` method.
- [x] Test Code: This time our `active_phrase` attribute should be a random phrase each time we run app.py.
      game = Game()
      print(game.active_phrase)
      print(game.active_phrase.phrase)

## Step 7:

### Head to the Phrase class inside the phrase.py file.

- [x] Inside the Phrase class, create a method called `display()`.
- [x] The `display` method will have two parameters: `self` and `guesses`.
- [x] It will need to take the `guesses` from the Game class so that it can compare the letters that have been guessed with the letters in the `phrase` attribute.
- [x] Loop through the letters in the `phrase` attribute.
- [x] If the letter was found in `self.phrase`, print the letter and then a space.
- [x] Otherwise, print an underscore “\_” followed by a space.
- [x] To keep this from printing each letter on new line, set the `end` attribute to be a space like so: print(f”{letter}”, end=” “)

- [] Test code: call the display method on the active_phrase and pass in the guesses attribute of the Game object.
  game = Game()
  print(game.active_phrase.phrase)
  game.active_phrase.display(game.guesses)

## Step 8:

### Create a welcome message for our game which will display at the start

- [x] Inside game.py create a new method called `welcome()`.
- [x] Test code:
      game = Game()
      game.welcome()
