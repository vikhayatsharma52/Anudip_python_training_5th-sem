# Daily Sales Performance Analyzer

sales = [15000, 22000, 18000, 25000, 30000, 17000, 28000, 26000, 21000, 19000]

# 1. Find the highest sales
highest_sales = max(sales)

# 2. Find the lowest sales
lowest_sales = min(sales)

# 3. Calculate average sales
average_sales = sum(sales) / len(sales)

# 4. Count days with sales above ₹20,000
count = 0
for sale in sales:
    if sale > 20000:
        count += 1

# 5. Display sales figures below average
below_average = []

for sale in sales:
    if sale < average_sales:
        below_average.append(sale)

# Display Results
print("Highest Sales: ₹{:,}".format(highest_sales))

print("\nLowest Sales: ₹{:,}".format(lowest_sales))

print("\nAverage Sales: ₹{:,.0f}".format(average_sales))

print("\nDays with Sales Above ₹20,000:", count)

print("\nSales Below Average:")
print(below_average)