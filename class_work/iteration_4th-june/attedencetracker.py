# Attendance Tracker

present = 0
absent = 0
student = 1

while student <= 30:
    status = input(f"Student {student} (P/A): ")

    if status.upper() == "P":
        present += 1
    else:
        absent += 1

    student += 1

print("Total Present Students:", present)
print("Total Absent Students:", absent)