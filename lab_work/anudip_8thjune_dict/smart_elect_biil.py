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

# 2. Find the highest-consuming house
highest_house = max(units, key=units.get)
print("\nHighest Consumption:")
print(highest_house, f"({units[highest_house]} units)")

# 3. Find the lowest-consuming house
lowest_house = min(units, key=units.get)
print("\nLowest Consumption:")
print(lowest_house, f"({units[lowest_house]} units)")

# 4. Calculate total units consumed
total_units = sum(units.values())
print("\nTotal Units Consumed:", total_units)

# 5. Create lists
low_consumption = [house for house, unit in units.items() if unit < 200]
medium_consumption = [house for house, unit in units.items() if 200 <= unit <= 400]
high_consumption = [house for house, unit in units.items() if unit > 400]

print("\nLow Consumption:")
print(low_consumption)

print("\nMedium Consumption:")
print(medium_consumption)

print("\nHigh Consumption:")
print(high_consumption)

# 6. Count houses eligible for an energy-saving campaign
eligible_count = sum(1 for unit in units.values() if unit > 300)
print("\nEligible for Energy-Saving Campaign:", eligible_count)