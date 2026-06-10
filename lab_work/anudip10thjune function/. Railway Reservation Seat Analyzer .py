seats = [
    "Booked", "Available", "Booked", "Booked",
    "Available", "Available", "Booked", "Available",
    "Booked", "Booked", "Available", "Booked"
]

# 1. Count seats
def count_seats(seats):
    booked = 0
    available = 0

    for seat in seats:
        if seat == "Booked":
            booked = booked + 1
        else:
            available = available + 1

    print("Booked Seats:", booked)
    print("Available Seats:", available)


# 2. First available seat
def first_available(seats):
    for i in range(len(seats)):
        if seats[i] == "Available":
            return i + 1


# 3. Occupancy percentage
def occupancy_percentage(seats):
    booked = 0

    for seat in seats:
        if seat == "Booked":
            booked = booked + 1

    percentage = (booked / len(seats)) * 100
    print("Occupancy Percentage:", percentage)


# 4. Display available seats
def display_available_seats(seats):
    print("Available Seat Numbers:")

    for i in range(len(seats)):
        if seats[i] == "Available":
            print(i + 1)


count_seats(seats)

print("First Available Seat:", first_available(seats))

occupancy_percentage(seats)

display_available_seats(seats)