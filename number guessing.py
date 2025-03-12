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