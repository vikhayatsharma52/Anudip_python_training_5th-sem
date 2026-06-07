n = int(input("Enter number of racers: "))

fastest_time = float('inf')
slowest_time = float('-inf')

fastest_pos = 0
slowest_pos = 0

for i in range(1, n + 1):
    lap_time = float(input(f"Enter lap time of racer {i}: "))

    if lap_time < fastest_time:
        fastest_time = lap_time
        fastest_pos = i

    if lap_time > slowest_time:
        slowest_time = lap_time
        slowest_pos = i

difference = slowest_time - fastest_time

print("Fastest Racer Position =", fastest_pos)
print("Slowest Racer Position =", slowest_pos)
print("Difference =", difference)