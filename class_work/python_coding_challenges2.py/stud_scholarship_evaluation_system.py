# Student Scholarship Evaluation System

# Dictionary storing student names and marks
marks = {
    "Anuj": 92,
    "Rahul": 76,
    "Priya": 88,
    "Neha": 64,
    "Amit": 58,
    "Sneha": 95,
    "Karan": 81,
    "Pooja": 73,
    "Rohit": 47,
    "Anjali": 90
}

# 1. Display students scoring above 85 marks
print("Students Scoring Above 85:")

for student, mark in marks.items():
    if mark > 85:
        print(student)

# 2. Find the topper
topper = max(marks, key=marks.get)

print("\nTopper:")
print(topper, "(", marks[topper], ")")

# 3. Find the student with the lowest marks
lowest = min(marks, key=marks.get)

print("\nLowest Scorer:")
print(lowest, "(", marks[lowest], ")")

# 4. Calculate class average marks
average = sum(marks.values()) / len(marks)

print("\nAverage Marks:", average)

# 5. Generate grades
print("\nGrades:")

for student, mark in marks.items():

    if mark >= 90:
        grade = "A"

    elif mark >= 75:
        grade = "B"

    elif mark >= 50:
        grade = "C"

    else:
        grade = "F"

    print(student, ":", grade)

# 6. Create a list of scholarship students
scholarship = []

for student, mark in marks.items():
    if mark >= 90:
        scholarship.append(student)

print("\nScholarship Students:")
print(scholarship)