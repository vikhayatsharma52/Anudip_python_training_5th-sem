# Attendance record
attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P']

# Count present and absent days
present = 0
absent = 0

for day in attendance:
    if day == 'P':          # Check present
        present += 1
    else:                   # Check absent
        absent += 1

print("Present Days:", present)
print("Absent Days:", absent)

# Calculate attendance percentage
percentage = (present / len(attendance)) * 100

print("\nAttendance Percentage:", percentage)

# Check eligibility
if percentage >= 75:
    print("Eligible")
else:
    print("Not Eligible")

# Display absent positions
print("\nAbsent Positions:")

for i in range(len(attendance)):
    if attendance[i] == 'A':
        print(i)