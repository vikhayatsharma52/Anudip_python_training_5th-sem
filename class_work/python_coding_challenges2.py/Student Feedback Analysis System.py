# Student Feedback Analysis System

file = open("feedback.txt", "r")

lines = file.readlines()

# 1. Count total lines
total_lines = len(lines)

# 2. Count total words
total_words = 0
for line in lines:
    total_words += len(line.split())

# 3. Count total characters
total_characters = 0
for line in lines:
    total_characters += len(line)

# 4. Find longest feedback comment
longest_feedback = max(lines, key=len).strip()

# 5. Find shortest feedback comment
shortest_feedback = min(lines, key=len).strip()

# 6. Count total vowels
vowels = 0
for line in lines:
    for ch in line.lower():
        if ch in "aeiou":
            vowels += 1

file.close()

# Display Results
print("Total Lines:", total_lines)
print("\nTotal Words:", total_words)
print("\nTotal Characters:", total_characters)

print("\nLongest Feedback:")
print(longest_feedback)

print("\nShortest Feedback:")
print(shortest_feedback)

print("\nTotal Vowels:", vowels)