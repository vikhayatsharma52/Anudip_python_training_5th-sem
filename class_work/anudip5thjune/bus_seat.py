# Bus Seat Reservation Analysis

seats = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]

booked = 0
available = 0
available_seats = []

# count booked and available seats
for i in range(len(seats)):

    if seats[i] == 1:
        booked += 1
    else:
        available += 1
        available_seats.append(i + 1)  # seat number starts from 1

# find first available seat
first_available = 0

for i in range(len(seats)):
    if seats[i] == 0:
        first_available = i + 1
        break   # stop searching immediately

# calculate occupancy percentage
occupancy = (booked / len(seats)) * 100

# display results
print("Booked Seats:", booked)
print("Available Seats:", available)
print("First Available Seat:", first_available)
print("Available Seat Numbers:", available_seats)
print("Bus Occupancy:", occupancy, "%")

# check occupancy status
if occupancy > 70:
    print("Status: More Than 70% Occupied")
else:
    print("Status: Not More Than 70% Occupied")