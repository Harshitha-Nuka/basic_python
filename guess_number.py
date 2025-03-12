"""
  A number guessing game where the program selects a random number between 1 and 20, 
  and the user must guess it. 
  Provide hints like "Too high" or "Too low".
  Make sure that the user is only entering values between 1 and 20 and the user has 
  maximum of 5 guesses. 
  If the user exceeds the max number of gusses then program
  should print "Game over!".

  Algorithm
  -----------------------
  Start
  Generate a random number between 1 and 20
  Set guess count to 1
  Repeat till User makes the correct guess or guess count reaches 5
  Accept the user input
  Verify the user input is between 1 and 20 and if not ask the user to input again
  If user input is less than random number print "Too Low"
  If user input is greater than random number print "Too High"
  If user input is same as random number print "Correct"
  End

"""
import random   # Python module named random

random_number = random.randint(1,20) # Generate a random number between 1 and 20
------------------------------------------------------------------------------

import random

def number_guessing_game():
    # Random number between 1 and 20
    secret_number = random.randint(1, 20)
    attempts = 5  # Maximum number of guesses

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 20.")
    print(f"You have {attempts} attempts to guess it.")

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}: Enter your guess: "))

            # Check if guess is within the valid range
            if guess < 1 or guess > 20:
                print("Please enter a number between 1 and 20.")
                continue

            # Check the guess
            if guess == secret_number:
                print(f"Congratulations! You guessed the number {secret_number} in {attempt} attempts.")
                break
            elif guess < secret_number:
                print("Too low!")
            else:
                print("Too high!")

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 20.")
    
    else:  # If loop ends without break (user ran out of attempts)
        print(f"Game over! The number was {secret_number}.")

# Run the game
number_guessing_game()
