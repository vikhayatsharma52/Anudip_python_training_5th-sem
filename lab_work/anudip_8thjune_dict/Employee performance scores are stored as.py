performance = {
    "EMP101": 92,
    "EMP102": 78,
    "EMP103": 45,
    "EMP104": 88,
    "EMP105": 97,
    "EMP106": 56,
    "EMP107": 81,
    "EMP108": 64,
    "EMP109": 39,
    "EMP110": 73
}

# 1. Display employees scoring above 80
print("Employees Scoring Above 80:")
for emp, score in performance.items():
    if score > 80:
        print(emp)

# 2. Count employees needing improvement (score < 60)
improvement_count = sum(1 for score in performance.values() if score < 60)
print("\nEmployees Needing Improvement:", improvement_count)

# 3. Find the top performer
top_employee = max(performance, key=performance.get)
print("\nTop Performer:", top_employee, f"({performance[top_employee]})")

# 4. Calculate average performance score
average_score = sum(performance.values()) / len(performance)
print("\nAverage Score:", round(average_score, 1))

# 5. Create separate lists
excellent = [emp for emp, score in performance.items() if score >= 90]
good = [emp for emp, score in performance.items() if 75 <= score <= 89]
average = [emp for emp, score in performance.items() if 60 <= score <= 74]
poor = [emp for emp, score in performance.items() if score < 60]

print("\nExcellent:")
print(excellent)

print("\nGood:")
print(good)

print("\nAverage:")
print(average)

print("\nPoor:")
print(poor)