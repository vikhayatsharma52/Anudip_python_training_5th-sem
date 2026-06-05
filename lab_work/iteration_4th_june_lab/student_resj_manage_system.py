# Student Result Management System

# Enter marks of 5 subjects
s1 = int(input("Subject 1 Marks: "))
s2 = int(input("Subject 2 Marks: "))
s3 = int(input("Subject 3 Marks: "))
s4 = int(input("Subject 4 Marks: "))
s5 = int(input("Subject 5 Marks: "))

# Calculate total and percentage
total = s1 + s2 + s3 + s4 + s5
percentage = total / 5

# Count failed subjects
fail_count = 0

if s1 < 40:
    fail_count += 1
if s2 < 40:
    fail_count += 1
if s3 < 40:
    fail_count += 1
if s4 < 40:
    fail_count += 1
if s5 < 40:
    fail_count += 1

# Find grade
if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "Fail"

# Show result
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)
print("Failed Subjects:", fail_count)