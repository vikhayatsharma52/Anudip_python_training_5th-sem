# Student Performance Analyzer

marks = [78, 45, 92, 35, 88, 40, 99, 56]

# list for passed students
passed = []

# list for merit students (marks above 75)
merit = []

# count failed students
failed_count = 0

# assume first mark is highest and lowest
highest = marks[0]
lowest = marks[0]

# check all marks
for mark in marks:

    # passed students
    if mark >= 40:
        passed.append(mark)
    else:
        failed_count += 1

    # merit list
    if mark > 75:
        merit.append(mark)

    # find highest mark
    if mark > highest:
        highest = mark

    # find lowest mark
    if mark < lowest:
        lowest = mark

# display results
print("Passed Students:", passed)
print("Failed Count:", failed_count)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Merit List:", merit)