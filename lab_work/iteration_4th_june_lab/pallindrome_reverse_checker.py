# Enter a number
num = int(input("Enter a Number: "))

# Store original number
temp = num
reverse = 0

# Find reverse number
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10

# Display reverse number
print("Reverse:", reverse)

# Check palindrome
if num == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")