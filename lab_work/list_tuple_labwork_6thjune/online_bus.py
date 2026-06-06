# Passenger count at each stop
passengers = [12, 18, 25, 30, 28, 15, 8]

# Find busiest stop
highest = passengers[0]

for p in passengers:
    if p > highest:
        highest = p

print("Busiest Stop Passengers:", highest)

# Display stops with fewer than 10 passengers
print("\nStops With Fewer Than 10 Passengers:")

for i in range(len(passengers)):
    if passengers[i] < 10:
        print("Stop", i)

# Calculate average passengers
total = 0

for p in passengers:
    total += p

average = total 