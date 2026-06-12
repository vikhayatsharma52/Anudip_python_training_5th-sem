# Mobile Screen Time Analyzer

# List storing screen time in minutes
screen_time = [180, 220, 150, 300, 120, 250, 190, 210, 175, 260]

# 1. Calculate average screen time
average = sum(screen_time) / len(screen_time)

print("Average Screen Time:", average, "minutes")

# 2. Find highest and lowest screen time
highest = max(screen_time)
lowest = min(screen_time)

print("\nHighest Screen Time:", highest, "minutes")
print("Lowest Screen Time:", lowest, "minutes")

# 3. Count days exceeding 200 minutes
count = 0

for time in screen_time:
    if time > 200:
        count += 1

print("\nDays Exceeding 200 Minutes:", count)

# 4. Display days with healthy usage
print("\nHealthy Usage Days:")

for i in range(len(screen_time)):
    if screen_time[i] < 180:
        print("Day", i + 1)

# 5. Categorize usage
healthy = 0
moderate = 0
excessive = 0

for time in screen_time:

    # Healthy usage
    if time < 180:
        healthy += 1

    # Moderate usage
    elif time <= 240:
        moderate += 1

    # Excessive usage
    else:
        excessive += 1

print("\nHealthy:", healthy)
print("Moderate:", moderate)
print("Excessive:", excessive)