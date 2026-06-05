# Enter employee details
name = input("Enter Employee Name: ")
basic_salary = float(input("Enter Basic Salary: "))

# Calculate HRA, DA and PF
hra = basic_salary * 20 / 100
da = basic_salary * 10 / 100
pf = basic_salary * 12 / 100

# Calculate salaries
gross_salary = basic_salary + hra + da
net_salary = gross_salary - pf

# Find employee grade
if net_salary > 50000:
    grade = "Senior Grade"
elif net_salary > 30000:
    grade = "Mid Grade"
else:
    grade = "Junior Grade"

# Display result
print("Employee Name:", name)
print("Gross Salary:", gross_salary)
print("Net Salary:", net_salary)
print("Grade:", grade)