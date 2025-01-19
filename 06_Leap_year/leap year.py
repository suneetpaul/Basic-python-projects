def is_leap_year(year):
    """Check if a given year is a leap year."""
    if year % 4 == 0:  # Year is divisible by 4
        if year % 100 == 0:  # Year is divisible by 100
            if year % 400 == 0:  # Year is divisible by 400
                print(f"{year} is a Leap Year.\n")
            else:
                print(f"{year} is not a Leap Year.\n")
        else:
            print(f"{year} is a Leap Year.\n")
    else:
        print(f"{year} is not a Leap Year.\n")

def main():
    """Main Function to Run the Leap Year Checker."""
    while True:
        status = input("Want to check for Leap Year? (y/n): ").lower()
        if status == 'y':
            year = int(input("Enter the Year: "))  # Prompt user for year input
            is_leap_year(year)               # Check if the entered year is a leap year
        else:
            print("Goodbye! 👋 See you next time.\n")
            break                         # Exit the loop and end the program

main()  # Call the main function to start the program
