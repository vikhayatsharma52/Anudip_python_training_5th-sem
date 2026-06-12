# Food Delivery Performance Dashboard

# List storing delivery times in minutes
delivery_times = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]

# 1. Find fastest delivery time
fastest = min(delivery_times)
print("Fastest Delivery:", fastest, "minutes")

# 2. Find slowest delivery time
slowest = max(delivery_times)
print("\nSlowest Delivery:", slowest, "minutes")

# 3. Calculate average delivery time
average = sum(delivery_times) / len(delivery_times)
print("\nAverage Delivery Time:", average, "minutes")

# 4. Display delayed orders
delayed_orders = []

for time in delivery_times:
    if time > 45:
        delayed_orders.append(time)

print("\nDelayed Orders:")
print(delayed_orders)

# 5. Categorize deliveries
fast = 0
normal = 0
delayed = 0

for time in delivery_times:

    # Fast delivery
    if time <= 30:
        fast += 1

    # Normal delivery
    elif time <= 45:
        normal += 1

    # Delayed delivery
    else:
        delayed += 1

print("\nFast Deliveries:", fast)
print("Normal Deliveries:", normal)
print("Delayed Deliveries:", delayed)