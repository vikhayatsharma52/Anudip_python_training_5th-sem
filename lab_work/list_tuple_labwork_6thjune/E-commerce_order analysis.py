# Order details
orders = [
    ("Laptop", 55000),
    ("Mouse", 800),
    ("Keyboard", 1500),
    ("Monitor", 12000),
    ("Pen Drive", 600)
]

# Display products costing more than 1000
print("Products Above ₹1000:")
for item in orders:
    if item[1] > 1000:
        print(item[0], item[1])

# Find most expensive product
expensive = orders[0]

for item in orders:
    if item[1] > expensive[1]:
        expensive = item

print("\nMost Expensive Product:")
print(expensive[0], expensive[1])

# Calculate total order value
total = 0

for item in orders:
    total += item[1]

print("\nTotal Order Value:", total)

# Count products below 1000
count = 0

for item in orders:
    if item[1] < 1000:
        count += 1

print("\nProducts Below ₹1000:", count)