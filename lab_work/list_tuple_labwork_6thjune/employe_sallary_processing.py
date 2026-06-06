# Employee data
employees = [
    ("Rahul", 35000),
    ("Priya", 55000),
    ("Amit", 42000),
    ("Neha", 65000)
]

# Display employees earning above 50000
print("Employees Earning Above ₹50000:")

for emp in employees:
    if emp[1] > 50000:      # Check salary
        print(emp[0], emp[1])

# Find highest-paid employee
highest = employees[0]

for emp in employees:
    if emp[1] > highest[1]: # Compare salary
        highest = emp

print("\nHighest Paid Employee:")
print(highest[0], highest[1])

# Calculate total salary expenditure
total = 0

for emp in employees:
    total += emp[1]         # Add salary

print("\nTotal Salary Expenditure:", total)

# Count employees earning below 40000
count = 0

for emp in employees:
    if emp[1] < 40000:      # Check salary
        count += 1

print("\nEmployees Below ₹40000:", count)