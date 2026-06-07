#8. Online Quiz Performance
#Sample Data
#quiz_scores = {
# "S001": 18,
# "S002": 12,
# "S003": 9,
# "S004": 20,
 #"S005": 14,
 #"S006": 7,
 #"S007": 16,
 #"S008": 10,
 #"S009": 19,
 ##"S010": 13
#}
#(Quiz is out of 20 marks.)
#Tasks
#• Display students scoring 15 or above.
#• Count students scoring below 10.
#• Find the top performer.
#• Create a list of students who passed (≥ 10 marks).
#• Calculate the class average. 

quiz_scores = {
    "S001": 18,
    "S002": 12,
    "S003": 9,
    "S004": 20,
    "S005": 14,
    "S006": 7,
    "S007": 16,
    "S008": 10,
    "S009": 19,
    "S010": 13
}

# Display students scoring 15 or above
print("Students scoring 15 or above:")
for student, marks in quiz_scores.items():
    if marks >= 15:
        print(student, "-", marks)

# Count students scoring below 10
count = 0
for marks in quiz_scores.values():
    if marks < 10:
        count += 1

print("\nStudents scoring below 10:", count)

# Find the top performer
top_student = max(quiz_scores, key=quiz_scores.get)
print("\nTop Performer:")
print(top_student, "-", quiz_scores[top_student])

# Create a list of students who passed
passed_students = []
for student, marks in quiz_scores.items():
    if marks >= 10:
        passed_students.append(student)

print("\nPassed Students:")
print(passed_students)

# Calculate the class average
total = 0
for marks in quiz_scores.values():
    total += marks

average = total / len(quiz_scores)

print("\nClass Average:", average)