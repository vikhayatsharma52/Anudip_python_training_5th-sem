# Correct and student answers
correct = ['A', 'C', 'B', 'D', 'A']
student = ['A', 'B', 'B', 'D', 'C']

# Count correct and wrong answers
correct_count = 0
wrong_count = 0

print("Wrong Question Numbers:")

for i in range(len(correct)):
    if correct[i] == student[i]:   # Check answer
        correct_count += 1
    else:
        wrong_count += 1
        print(i + 1)               # Question number

# Calculate score
score = correct_count

print("\nScore:", score)

# Display counts
print("Correct Answers:", correct_count)
print("Wrong Answers:", wrong_count)

# Calculate percentage
percentage = (correct_count / len(correct)) * 100

print("Percentage:", percentage)

# Check pass or fail
if percentage >= 60:
    print("Pass")
else:
    print("Fail")