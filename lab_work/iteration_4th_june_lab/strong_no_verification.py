 #Write a program to check whether a given number is a Strong Number.
# Strong Number Verification

num = int(input("Enter a Number: "))

temp = num
sum = 0

while temp > 0:

    digit = temp % 10      

    fact = 1
    for i in range(1, digit + 1):

        #find factorial
        fact = fact * i  

  # add factorial to sum
    sum = sum + fact       

    #remove last digit

    temp = temp // 10      

if sum == num:
    print(num, "is a Strong Number")
else:
    print(num, "is not a Strong Number")