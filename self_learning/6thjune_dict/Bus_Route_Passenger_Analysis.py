#7. Bus Route Passenger Analysis
#Sample Data
#passengers = {
# "Stop1": 12,
# "Stop2": 25,
# "Stop3": 18,
# "Stop4": 32,
# "Stop5": 9,
# "Stop6": 28,
# "Stop7": 14,
# "Stop8": 7,
# "Stop9": 21,
# "Stop10": 16
#}
#Tasks
#• Display stops having more than 20 passengers.
#• Count stops with fewer than 10 passengers.
#• Find the busiest stop.
#• Create a list of stops requiring an extra bus (passengers > 25).
#• Calculate the average number of passengers. 

passengers = {
    "Stop1": 12,
    "Stop2": 25,
    "Stop3": 18,
    "Stop4": 32,
    "Stop5": 9,
    "Stop6": 28,
    "Stop7": 14,
    "Stop8": 7,
    "Stop9": 21,
    "Stop10": 16
}

# Display stops having more than 20 passengers
print("Stops having more than 20 passengers:")
for stop, count in passengers.items():
    if count > 20:
        print(stop, "-", count)

# Count stops with fewer than 10 passengers
low_count = 0
for count in passengers.values():
    if count < 10:
        low_count += 1

print("\nStops with fewer than 10 passengers:", low_count)

# Find the busiest stop
busiest_stop = max(passengers, key=passengers.get)
print("\nBusiest Stop:")
print(busiest_stop, "-", passengers[busiest_stop])

# Create a list of stops requiring an extra bus
extra_bus = []
for stop, count in passengers.items():
    if count > 25:
        extra_bus.append(stop)

print("\nStops requiring an extra bus:")
print(extra_bus)

# Calculate the average number of passengers
total = 0
for count in passengers.values():
    total += count

average = total / len(passengers)

print("\nAverage Number of Passengers:", average)