# Employee Performance Evaluation System

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
improvement_count = 0

for score in performance.values():
    if score < 60:
        improvement_count += 1

print("\nEmployees Needing Improvement:", improvement_count)

# 3. Find the top performer
top_employee = max(performance, key=performance.get)

print("\nTop Performer:")
print(top_employee, "(", performance[top_employee], ")", sep="")

# 4. Calculate average performance score
average_score = sum(performance.values()) / len(performance)

print("\nAverage Score:", round(average_score, 1))

# 5. Categorize employees
excellent = []
good = []
average = []
poor = []

for emp, score in performance.items():

    if score >= 90:
        excellent.append(emp)

    elif score >= 75:
        good.append(emp)

    elif score >= 60:
        average.append(emp)

    else:
        poor.append(emp)

print("\nExcellent:")
print(excellent)

print("\nGood:")
print(good)

print("\nAverage:")
print(average)

print("\nPoor:")
print(poor)