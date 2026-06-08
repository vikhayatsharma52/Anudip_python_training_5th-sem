sales = {
    "Laptop": 15,
    "Mouse": 45,
    "Keyboard": 32,
    "Monitor": 12,
    "Headphones": 28,
    "Printer": 8,
    "Webcam": 20,
    "Speaker": 18,
    "Tablet": 10,
    "Router": 25
}

# 1. Display products sold more than 20 times
print("Products Sold More Than 20 Times:")
for product, count in sales.items():
    if count > 20:
        print(product)

# 2. Find the best-selling product
best_product = max(sales, key=sales.get)
print("\nBest Selling Product:", best_product, f"({sales[best_product]})")

# 3. Find the least-selling product
least_product = min(sales, key=sales.get)
print("\nLeast Selling Product:", least_product, f"({sales[least_product]})")

# 4. Calculate total products sold
total_sold = sum(sales.values())
print("\nTotal Units Sold:", total_sold)

# 5. Create a list of products requiring promotion (sales < 15)
promotion_products = [product for product, count in sales.items() if count < 15]
print("\nProducts Requiring Promotion:")
print(promotion_products)

# 6. Count products having sales between 10 and 30
count_products = sum(1 for count in sales.values() if 10 <= count <= 30)
print("\nProducts Having Sales Between 10 and 30:", count_products)