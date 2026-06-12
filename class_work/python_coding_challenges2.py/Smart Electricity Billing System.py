# Smart Electricity Billing System

# Dictionary storing house numbers and electricity units
units = {
    "House101": 320,
    "House102": 180,
    "House103": 510,
    "House104": 275,
    "House105": 150,
    "House106": 430,
    "House107": 220,
    "House108": 390,
    "House109": 145,
    "House110": 600
}

# 1. Display houses consuming more than 400 units
print("Houses Consuming More Than 400 Units:")
for house, unit in units.items():
    if unit > 400:
        print(house)

# 2. Find highest-consuming house
highest_house = max(units, key=units.get)
print("\nHighest Consumption:")
print(highest_house, "(", units[highest_house], "units )")

# 3. Find lowest-consuming house
lowest_house = min(units, key=units.get)
print("\nLowest Consumption:")
print(lowest_house, "(", units[lowest_house], "units )")

# 4. Calculate total units consumed
total_units = sum(units.values())
print("\nTotal Units Consumed:", total_units)

# 5. Create separate lists
low = []
medium = []
high = []

for house, unit in units.items():

    # Less than 200 units
    if unit < 200:
        low.append(house)

    # Between 200 and 400 units
    elif unit <= 400:
        medium.append(house)

    # More than 400 units
    else:
        high.append(house)

print("\nLow Consumption:")
print(low)

print("\nMedium Consumption:")
print(medium)

print("\nHigh Consumption:")
print(high)

# 6. Count houses with consumption more than 300 units
count = 0

for unit in units.values():
    if unit > 300:
        count += 1

print("\nEligible for Energy-Saving Campaign:", count)