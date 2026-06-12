# Student Attendance Percentage Calculator

attendance = ('P', 'P', 'A', 'P', 'P', 'P', 'A', 'A', 'P', 'P', 'P', 'P', 'A', 'P', 'P')

# 1. Count present days
present_days = attendance.count('P')

# 2. Count absent days
absent_days = attendance.count('A')

# 3. Calculate attendance percentage
total_days = len(attendance)
attendance_percentage = (present_days / total_days) * 100

# Display results
print("Present Days:", present_days)

print("\nAbsent Days:", absent_days)

print("\nAttendance Percentage: {:.2f}%".format(attendance_percentage))

# 4 & 5. Determine attendance status
print("\nAttendance Status:")

if attendance_percentage < 75:
    print("Below 75%")
else:
    print("Above 75%")