# Consecutive Number Detector

numbers = [4, 5, 6, 10, 11, 15, 16, 17]

# list to store consecutive pairs
pairs = []

# check consecutive numbers
for i in range(len(numbers) - 1):

    # if difference is 1, numbers are consecutive
    if numbers[i + 1] - numbers[i] == 1:

        print(numbers[i], "and", numbers[i + 1], "are consecutive")

        # store pair in list
        pairs.append((numbers[i], numbers[i + 1]))

# display all pairs
print("Consecutive Pairs:", pairs)