"""
Project Name: Random Number Generator
Author: Freddy Salas Miranda
Date: 2024-05-12
GitHub: https://github.com/FSalasm

Description:
This program generates a random number within a user-defined range, 
accommodating user inputs for both the lower and upper bounds 
(e.g., 1 to 10, or 5 to 20). It features a graphical user interface (GUI), 
making it more accessible and user-friendly compared to traditional command-line applications. 
Users can effortlessly set the desired range through text fields and trigger the number generation with a simple button click.
"""

import tkinter as tk
import random
from tkinter import messagebox

def generate_random_number():
    """
    Generates a random integer within the user-specified range
    and displays it in the result label.
    Validates the input to ensure they are integers and that
    the minimum value is less than the maximum value.
    """
    try:
        # Get the minimum and maximum values from the entry widgets
        min_val = int(min_entry.get())
        max_val = int(max_entry.get())

        # Check if the minimum value is less than the maximum value
        if min_val >= max_val:
            # Display an error message if the condition is not met
            messagebox.showerror("Error", "The minimum value must be less than the maximum value.")
            return

        # Generate a random number within the specified range
        random_number = random.randint(min_val, max_val)
        # Update the result label with the generated random number
        result_label.config(text=f"The generated random number is: {random_number}")
    except ValueError:
        # Display an error message if the input values are not valid integers
        messagebox.showerror("Error", "Invalid input. Please enter integers for both fields.")

def create_gui():
    """
    Creates the main GUI window for the random number generator.
    Sets up the layout and widgets for user interaction.
    """
    # Create the main window
    root = tk.Tk()
    root.title("Random Number Generator")

    # Create and place widgets
    global min_entry, max_entry, result_label

    # Label and entry for minimum value
    tk.Label(root, text="Enter the minimum value:").pack(pady=5)
    min_entry = tk.Entry(root)
    min_entry.pack(pady=5)

    # Label and entry for maximum value
    tk.Label(root, text="Enter the maximum value:").pack(pady=5)
    max_entry = tk.Entry(root)
    max_entry.pack(pady=5)

    # Button to trigger the random number generation
    generate_button = tk.Button(root, text="Generate Random Number", command=generate_random_number)
    generate_button.pack(pady=10)

    # Label to display the result
    result_label = tk.Label(root, text="")
    result_label.pack(pady=10)

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    create_gui()
