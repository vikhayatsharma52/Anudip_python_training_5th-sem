# Program to check whether a number is prime or not

# Prime Number Analyzer

num = int(input("Enter a Number: "))
count = 0

for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")
        count += 1

print()

if count == 2:
    print(num, "is a Prime Number")
else:
    print(num, "is not a Prime Number")