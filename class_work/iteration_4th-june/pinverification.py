# PIN Verification

pin = 0

while pin != 1234:
    pin = int(input("Enter PIN: "))

    if pin != 1234:
        print("Incorrect PIN. Try Again.")

print("Access Granted")