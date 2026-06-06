# Student records stored in tuple
students = (
    (101, "Rahul", "Python", 25000),
    (102, "Priya", "Java", 30000),
    (103, "Amit", "Data Science", 45000),
    (104, "Sneha", "Python", 25000),
    (105, "Rohan", "MERN", 40000)
)

# 1. Display all student records
print("All Student Records:")
for s in students:
    print(s)

# 2. Display first student details
print("\nFirst Student:")
print(students[0])

# 3. Display last student details
print("\nLast Student:")
print(students[-1])

# 4. Display Student ID and Name
print("\nStudent ID and Name:")
for s in students:
    print(s[0], s[1])

# 5. Count total students
print("\nTotal Students:", len(students))

# 6. Check if Rahul exists
found = False

for s in students:
    if s[1] == "Rahul":
        found = True

if found:
    print("\nRahul exists in records")
else:
    print("\nRahul does not exist")