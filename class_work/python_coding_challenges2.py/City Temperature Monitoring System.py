temperature = {
    "Delhi": 41,
    "Mumbai": 33,
    "Chennai": 37,
    "Kolkata": 39,
    "Bengaluru": 28,
    "Pune": 30,
    "Jaipur": 42,
    "Lucknow": 40,
    "Hyderabad": 35,
    "Ahmedabad": 43
}

# 1. Cities with temperature above 40°C
print("Cities Above 40°C:")
for city, temp in temperature.items():
    if temp > 40:
        print(city)

# 2. Hottest city
hottest_city = max(temperature, key=temperature.get)
print("\nHottest City:")
print(hottest_city, "(", temperature[hottest_city], "°C)", sep="")

# 3. Coolest city
coolest_city = min(temperature, key=temperature.get)
print("\nCoolest City:")
print(coolest_city, "(", temperature[coolest_city], "°C)", sep="")

# 4. Average temperature
average = sum(temperature.values()) / len(temperature)
print("\nAverage Temperature:", round(average, 1), "°C")

# 5. Pleasant cities (<35°C)
pleasant_cities = []

for city, temp in temperature.items():
    if temp < 35:
        pleasant_cities.append(city)

print("\nPleasant Cities:")
print(pleasant_cities)
