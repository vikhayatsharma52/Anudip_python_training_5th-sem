# Employee Salary Report Generator

file = open("employees.txt", "r")

employees = []
salaries = []

for line in file:
    emp_id, name, salary = line.strip().split(",")
    salary = int(salary)

    employees.append((emp_id, name, salary))
    salaries.append(salary)

file.close()

# 1. Employees earning more than ₹50,000
print("Employees Earning Above ₹50,000:")
for emp in employees:
    if emp[2] > 50000:
        print(emp[1])

# 2. Highest-paid employee
highest = max(employees, key=lambda x: x[2])

print("\nHighest Paid Employee:")
print(f"{highest[1]} (₹{highest[2]:,})")

# 3. Lowest-paid employee
lowest = min(employees, key=lambda x: x[2])

print("\nLowest Paid Employee:")
print(f"{lowest[1]} (₹{lowest[2]:,})")

# 4. Average salary
average = sum(salaries) / len(salaries)

print("\nAverage Salary: ₹", round(average), sep="")

# 5. Salary Categories
high = []
medium = []
low = []

for emp in employees:
    name = emp[1]
    salary = emp[2]

    if salary >= 60000:
        high.append(name)
    elif salary >= 40000:
        medium.append(name)
    else:
        low.append(name)

print("\nHigh Salary:")
print(high)

print("\nMedium Salary:")
print(medium)

print("\nLow Salary:")
print(low)