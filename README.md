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

## Step 9:

### Head back to game.py and create a new method called `start()`

- [x] This method will start by calling the `welcome()` method to display the welcome,
- [x] printing the number of misses (or incorrect guesses), and
- [x] displaying the active phrase

#### Inside start, call the `welcome()` method.

- [x] Add a print statement to print out “Number missed: “ followed by `self.missed`,
- [x] then call the `display()` method on the `active_phrase` attribute.
- [x] Don’t forget to pass in `self.guesses` to the `display()` method.
- [x] Test Code: Back in app.py create your Game instance. For the purposes of testing, print out the `phrase` attribute of the Phrase instance stored in `active_phrase`. Run the `start()` method on the Game object.
      game = Game()
      print(game.active_phrase.phrase)
      game.start()

## Step 10:

### Start adding some user interaction to the game

#### Create a method to get the user’s guess and store it

- [x] In game.py, create a new method named `get_guess`.
- [x] This method should prompt the user for a guess and return the user’s input.
- [x] Inside the `start()` method, create a new variable named `user_guess` and assign it the input that is returned by the `get_guess()` method.
- [x] Append `user_guess` to the `guesses` attribute.

#### Test Code:

- [x] print the `user_guess` after it received the value returned by `get_guess`
- [x] call the `display` method on the `active_phrase` attribute to make sure it is working properly.

## Step 11:

### Check if the user got the letter incorrect.

- [x] in phrase.py create a method named `check_guess`
- [x] Besides `self`, it will also take a parameter for `guess`.
- [x] send in the `user_guess`
- [x] It should return `True`, if the guess was correct and `False` if the guess was incorrect.

#### Test Code:

- [x] Inside your `start` method in game.py after you have appended the `user_guess` to `guesses`,
- [x] call the `check_guess` method on the `active_phrase` attribute and send in the `user_guess`.
- [x] The following code should print “YAY” if the guess was correct and “Bummer!” if it was incorrect:

## Step 12:

### start adding to the `missed` attribute in the case that the user guesses incorrectly and begin the loop that will continue until the game is either won or lost.

- [x] remove the `bummer` print statement
- [x] negate: `if not self.active_phrase.check_guess(user_guess):`
- [x] add a `while` loop to keep this going as long as the number of `missed` is less than 5
- [x] Because the welcome should only be shown once, this should be added immediately below the call to the `welcome` method.
- [x] Test Code: The game should end when you’ve guessed five times incorrectly

## Step 13:

### handle when the user wins the game

- [x] Inside the phrase.py class, create a new method called `check_complete`.
- [x] The method should return `True` if all letters have been guessed and `False` if any character has not been guessed.
- [x] Besides `self`, this method will also have a parameter of `guesses` and
- [x] we’ll need to pass in the `guesses` attribute from the Game class.
- [x] Loop through the `phrase` attribute.
- [x] If any letter is not present in `guesses`, return `False`.
- [x] If it makes it through the entire loop without returning `False`, return `True`.

- [x] In game.py, change your `while` loop so that it runs while `missed` is less than five and calling `check_complete` returns `False`.

## Step 14:

### Add polish, either congratulate the user or tell them that they lost

- [x] Inside game.py create a new method named `game_over`.
- [x] If the number `missed` is equal to the five print out a message to the user that they lost the game.
- [x] Otherwise, print out a congratulatory message and tell them that they won.
- [x] Place the call to `game_over()` after the `while` loop.
