# Parking slots
slots = [1, 0, 1, 1, 0, 0, 1, 0]

# Count occupied and available slots
occupied = 0
available = 0

for slot in slots:
    if slot == 1:          # Check occupied slot
        occupied += 1
    else:                  # Check available slot
        available += 1

print("Occupied Slots:", occupied)
print("Available Slots:", available)

# Find first available slot
for i in range(len(slots)):
    if slots[i] == 0:      # Check available slot
        print("\nFirst Available Slot:", i)
        break              # Stop after first available slot

# Display all available slot numbers
print("\nAvailable Slot Numbers:")

for i in range(len(slots)):
    if slots[i] == 0:
        print(i)

# Check occupancy percentage
occupancy = (occupied / len(slots)) * 100

print("\nOccupancy Percentage:", occupancy)

if occupancy > 75:
    print("Parking Occupancy Exceeds 75%")
else:
    print("Parking Occupancy is Below 75%")