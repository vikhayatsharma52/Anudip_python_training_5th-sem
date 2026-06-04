 # programn Accept a number from the user and check whether it is an Armstrong Number.

num = int(input("Enter Number: "))

temp = num
total = 0

while temp > 0:
    digit = temp % 10
    total = total + digit * digit * digit
    temp = temp // 10

if total == num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")