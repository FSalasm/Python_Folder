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

def roll_dice(num_dice, sides):
    """
    Rolls a specified number of dice with a specified number of sides.

    Parameters:
    num_dice (int): The number of dice to roll.
    sides (int): The number of sides on each die.

    Returns:
    list: A list containing the results of each die rolled.
    """
    rolls = [generate_random_number(1, sides) for _ in range(num_dice)]
    return rolls

def main():
    """
    Main program function that orchestrates user interactions and dice rolling.

    Prompts the user to enter the number of dice and the number of sides per die, 
    then rolls the dice and displays the results.
    """
    print("Welcome to the Dice Roller!")

    while True:
        num_dice = get_validated_input("Enter the number of dice to roll: ")
        sides = get_validated_input("Enter the number of sides on each die: ")

        if num_dice <= 0 or sides <= 0:
            print("The number of dice and sides must be greater than zero.")
            continue

        rolls = roll_dice(num_dice, sides)
        print(f"Rolls: {rolls}")
        print(f"Total: {sum(rolls)}")

        continue_running = input("Do you want to roll again? (yes/no): ").lower()
        if continue_running != "yes" or "y":
            print("Exiting the Dice Roller. Goodbye!")
            break

if __name__ == "__main__":
    main()