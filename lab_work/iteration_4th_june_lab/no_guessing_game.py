import random

# generate a random number between 1 and 50
secret_number = random.randint(1, 50)

attempts = 0

# keep asking until correct guess
while True:
    
    guess = int(input("Enter your guess (1-50): "))
    
    # count attempts
    attempts += 1

    if guess > secret_number:
        print("Too High")

    elif guess < secret_number:
        print("Too Low")

    else:
        print("Correct Guess")
        print("Total Attempts:", attempts)
        break