# Password Strength Analyzer

password = "Python@2026!"

upper = 0
lower = 0
digits = 0
special = 0

digit_list = []
special_list = []

for ch in password:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digits += 1
        digit_list.append(ch)
    else:
        special += 1
        special_list.append(ch)

# Password Strength Check
if (len(password) >= 8 and upper >= 1 and lower >= 1
        and digits >= 1 and special >= 1):
    strength = "Strong"
elif len(password) >= 6:
    strength = "Medium"
else:
    strength = "Weak"

print("Password:", password)

print("\nUppercase Letters:", upper)
print("Lowercase Letters:", lower)
print("Digits:", digits)
print("Special Characters:", special)

print("\nDigits Found:", digit_list)
print("Special Characters Found:", special_list)

print("\nPassword Strength:", strength)