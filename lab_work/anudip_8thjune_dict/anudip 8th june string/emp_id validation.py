# Employee ID Validation and Analysis System

emp_id = "EMP2026ANUJ458"

print("Employee ID:", emp_id)

# 1. Count uppercase letters
upper_count = 0
for ch in emp_id:
    if ch.isupper():
        upper_count += 1

# 2. Count digits
digit_count = 0
for ch in emp_id:
    if ch.isdigit():
        digit_count += 1

# 3. Extract joining year
year = emp_id[3:7]

# 4. Extract employee name
name = emp_id[7:-3]

# 5. Validate ID
valid = (
    emp_id.startswith("EMP") and
    year.isdigit() and len(year) == 4 and
    emp_id[-3:].isdigit() and len(emp_id[-3:]) == 3
)

# 6. Create list of digits
digit_list = []
for ch in emp_id:
    if ch.isdigit():
        digit_list.append(int(ch))

# 7. Sum of digits
digit_sum = sum(digit_list)

# 8. Display results
print("\nUppercase Letters:", upper_count)
print("Digits:", digit_count)

print("\nJoining Year:", year)
print("Employee Name:", name)

print("\nDigit List:", digit_list)
print("Sum of Digits:", digit_sum)

if valid:
    print("\nID Status: Valid")
else:
    print("\nID Status: Invalid")