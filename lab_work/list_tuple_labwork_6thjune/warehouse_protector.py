# Product IDs and quality status
products = [
    (101, "Pass"),
    (102, "Fail"),
    (103, "Pass"),
    (104, "Fail"),
    (105, "Pass")
]

# Display failed product IDs
print("Failed Product IDs:")

for p in products:
    if p[1] == "Fail":      # Check status
        print(p[0])

# Count passed and failed products
passed = 0
failed = 0

for p in products:
    if p[1] == "Pass":
        passed += 1
    else:
        failed += 1

print("\nPassed Products:", passed)
print("Failed Products:", failed)

# Calculate pass percentage
percentage = (passed / len(products)) * 100

print("Pass Percentage:", percentage)

# Stop checking if 3 failures are found
fail_count = 0

for p in products:
    if p[1] == "Fail":
        fail_count += 1

    if fail_count == 3:
        print("3 Failures Found")
        break