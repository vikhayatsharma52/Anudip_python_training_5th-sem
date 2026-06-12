# Shopping Cart Billing System

prices = (1250, 799, 450, 999, 300, 1500, 650, 250, 850, 1200)

# 1. Calculate total bill amount
total_bill = sum(prices)

# 2. Find most expensive product
most_expensive = max(prices)

# 3. Find least expensive product
least_expensive = min(prices)

# 4. Count products costing more than ₹1000
count = 0
for price in prices:
    if price > 1000:
        count += 1

# 5. Create discount eligible products list (price > ₹800)
discount_products = []

for price in prices:
    if price > 800:
        discount_products.append(price)

# Display Results
print("Total Bill Amount: ₹", total_bill, sep="")

print("\nMost Expensive Product: ₹", most_expensive, sep="")

print("\nLeast Expensive Product: ₹", least_expensive, sep="")

print("\nProducts Costing More Than ₹1000:", count)

print("\nDiscount Eligible Products:")
print(discount_products)