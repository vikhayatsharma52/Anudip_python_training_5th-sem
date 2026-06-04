# Guess the Number Game

# Initialize guess with a value other than 7
guess = 0

# Repeat until the correct number is guessed
while guess != 7:

    # Take input from the user
    guess = int(input("Guess the Number: "))

    # Check if the guess is wrong
    if guess != 7:
        print("Wrong Guess. Try Again.")

