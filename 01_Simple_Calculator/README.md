#Simple Calculator Program

This project is a basic calculator program implemented in Python. It allows users to 
perform four fundamental arithmetic operations: addition, subtraction, multiplication, and division. 
The program runs in a loop, continuously prompting the user to choose an operation or exit the program.

Key Features:

Operations Supported:

Addition (add): Adds two numbers.
Subtraction (sub): Subtracts the second number from the first.
Multiplication (mult): Multiplies two numbers.
Division (div): Divides the first number by the second, with a check to prevent division by zero.

User Interaction:
The program prompts the user to select an operation (add, sub, mult, div) or exit the program (exit).
After selecting an operation, the user is asked to input two numbers.
The program then performs the selected operation and displays the result.


Error Handling:
The program checks for division by zero and displays an error message if attempted.
It also handles invalid user inputs by displaying an "invalid input" message.

Looping Mechanism:
The program runs in an infinite loop, allowing the user to perform multiple calculations without restarting the program.
The loop can be exited by typing exit, which displays a "goodbye" message and terminates the program.


Functions:
add(x, y): Adds x and y and prints the result.
sub(x, y): Subtracts y from x and prints the result.
mul(x, y): Multiplies x and y and prints the result.
div(x, y): Divides x by y, checks for division by zero, and prints the result or an error message.

Main Loop:
Continuously prompts the user for input.
Calls the appropriate function based on the user's choice.
Handles invalid inputs and provides an option to exit the program.

Example Usage:
User inputs add, then provides two numbers (e.g., 5 and 3). The program outputs 8.
User inputs div, then provides two numbers (e.g., 10 and 0). The program outputs Error: Division by zero is not allowed.
User inputs exit. The program outputs good bye and terminates.


This project serves as a foundational example of how to create a simple, interactive program in Python, 
demonstrating basic programming concepts such as functions, loops, conditionals, and user input handling.
