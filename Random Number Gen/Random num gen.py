"""
Project Name: Random Number Generator
Author: Freddy Salas Miranda
Date: 2024-05-02
GitHub: https://github.com/FSalasm

Description:
This program generates a random number within a user-defined range. The user can specify the lower and upper bounds of the range 
(e.g., 1 to 10, or 5 to 20), making the tool versatile for various applications, from games to simulation exercises. 
It's designed to be user-friendly and demonstrate basic programming concepts like input handling and random number generation.
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

def main():
    """
    Main program function that orchestrates user interactions and random number generation.
    
    Continuously prompts the user to enter a minimum and maximum range, generates a random number within that range, 
    and allows the user to repeat the process or exit.
    """
    print("Welcome to the Configurable Random Number Generator!")

    while True:
        min_val = get_validated_input("Enter the minimum value for the range: ")
        max_val = get_validated_input("Enter the maximum value for the range: ")

        if min_val >= max_val:
            print("The minimum value must be less than the maximum value.")
            continue

        random_number = generate_random_number(min_val, max_val)
        print(f"The generated random number is: {random_number}")

        continue_running = input("Do you want to generate another number? (yes/no): ").lower()
        if continue_running != 'yes':
            print("Exiting the Random Number Generator. Goodbye!")
            break

if __name__ == "__main__":
    main()
