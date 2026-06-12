# Library Book Issue Tracker

book_issues = [15, 8, 22, 10, 18, 5, 30, 12, 20, 25]

# 1. Find maximum issues
maximum = max(book_issues)

# 2. Find minimum issues
minimum = min(book_issues)

# 3. Calculate average issues
average = sum(book_issues) / len(book_issues)

# 4. Count books issued more than 15 times
count = 0
for issues in book_issues:
    if issues > 15:
        count += 1

# 5. Create a list of books issued fewer than 10 times
less_than_10 = []

for issues in book_issues:
    if issues < 10:
        less_than_10.append(issues)

# Display Results
print("Maximum Issues:", maximum)

print("\nMinimum Issues:", minimum)

print("\nAverage Issues:", average)

print("\nBooks Issued More Than 15 Times:", count)

print("\nBooks Issued Fewer Than 10 Times:")
print(less_than_10)