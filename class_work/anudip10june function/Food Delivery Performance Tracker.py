delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]

# Find fastest delivery
def fastest_delivery(times):
    return min(times)

# Find delayed orders
def delayed_orders(times):
    delayed = []

    for time in times:
        if time > 45:
            delayed.append(time)

    return delayed

# Find average delivery time
def average_delivery_time(times):
    total = 0

    for time in times:
        total = total + time

    return total / len(times)

# Display categories
def delivery_category(times):
    for time in times:

        if time <= 30:
            print(time, "-> Fast")

        elif time <= 45:
            print(time, "-> Normal")

        else:
            print(time, "-> Delayed")


# Function Calls
print("Fastest Delivery:", fastest_delivery(delivery_time), "minutes")

print("\nDelayed Orders:")
print(delayed_orders(delivery_time))

print("\nAverage Delivery Time:")
print(average_delivery_time(delivery_time), "minutes")

print("\nCategories:")
delivery_category(delivery_time)