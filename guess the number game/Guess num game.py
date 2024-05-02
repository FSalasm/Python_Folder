"""
Project Name: Guess The Number Game
Author: Freddy Salas Miranda
Date: 2024-05-02
GitHub: https://github.com/FSalasm
"""

import random

def generate_random_number(min_val, max_val):
    """
    Generates a random integer within a user-specified range.
    
    Parameters:
    min_val (int): The lower bound of the range.
    max_val (int): The upper bound of the range.
    
    Returns:
    int: A random integer between min_val and max_val.
    """
    return random.randint(min_val, max_val)

def get_validated_input(prompt):
    """
    Prompts the user for input and validates it to ensure it is an integer.
    
    Parameters:
    prompt (str): The prompt message displayed to the user.
    
    Returns:
    int: The user-inputted integer after validation.
    """
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

def play_game(min_val, max_val, max_attempts):
    """
    Core game logic for guessing the number with hints and scoring system.
    
    Parameters:
    min_val (int): The minimum value of the range.
    max_val (int): The maximum value of the range.
    max_attempts (int): The maximum number of guesses allowed.
    """
    number_to_guess = generate_random_number(min_val, max_val)
    guesses = 0

    while guesses < max_attempts:
        print(f"Attempt {guesses + 1} of {max_attempts}.")
        guess = get_validated_input(f"Guess a number between {min_val} and {max_val}: ")
        guesses += 1

        if guess == number_to_guess:
            print("Congratulations! You've guessed the right number.")
            return 10 - 2 * (guesses - 1)  # scoring system
        elif guesses == max_attempts:
            print(f"Sorry, the correct number was {number_to_guess}. You've lost this round.")
            return 0
        else:
            if guess < number_to_guess:
                print("Higher!")
            else:
                print("Lower!")

    return 0  # in case all attempts are used up without correct guess

def main():
    print("Welcome to the Number Guessing Game!")

    score = 0
    while True:
        print(f"Current Score: {score}")
        print("Choose a difficulty level:")
        print("1. Easy (1-20)")
        print("2. Normal (1-100)")
        print("3. Hard (1-500)")
        print("4. Custom")
        choice = get_validated_input("Select option (1-4): ")

        if choice == 1:
            score += play_game(1, 20, 4)
        elif choice == 2:
            score += play_game(1, 100, 6)
        elif choice == 3:
            score += play_game(1, 500, 8)
        elif choice == 4:
            custom_min = get_validated_input("Enter custom range minimum value: ")
            custom_max = get_validated_input("Enter custom range maximum value: ")
            custom_attempts = get_validated_input("Enter custom number of attempts allowed: ")
            if custom_min < custom_max:
                score += play_game(custom_min, custom_max, custom_attempts)
            else:
                print("Invalid range. Minimum must be less than maximum.")
                continue

        if input("Play again? (yes/no): ").lower() != 'yes':
            print(f"Final Score: {score}")
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()