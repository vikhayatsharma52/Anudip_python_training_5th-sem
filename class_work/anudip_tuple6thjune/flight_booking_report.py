# Flight booking records
bookings = (
    ("P101", "Delhi", "Confirmed"),
    ("P102", "Mumbai", "Waiting"),
    ("P103", "Delhi", "Confirmed"),
    ("P104", "Chennai", "Cancelled"),
    ("P105", "Mumbai", "Confirmed"),
    ("P106", "Delhi", "Waiting")
)

# Show confirmed passengers
print("Confirmed Passengers:")
for p in bookings:
    if p[2] == "Confirmed":
        print(p[0], p[1])

# Count Delhi passengers
count = 0
for p in bookings:
    if p[1] == "Delhi":
        count += 1

print("\nDelhi Passengers:", count)

# Count booking status
confirmed = 0
waiting = 0
cancelled = 0

for p in bookings:
    if p[2] == "Confirmed":
        confirmed += 1
    elif p[2] == "Waiting":
        waiting += 1
    else:
        cancelled += 1

print("\nConfirmed:", confirmed)
print("Waiting:", waiting)
print("Cancelled:", cancelled)

# Create waiting list
waiting_list = []

for p in bookings:
    if p[2] == "Waiting":
        waiting_list.append(p[0])

print("\nWaiting List:", waiting_list)

# Find most booked destination
destinations = []

for p in bookings:
    destinations.append(p[1])

most_booked = max(destinations, key=destinations.count)

print("\nMost Booked Destination:", most_booked)