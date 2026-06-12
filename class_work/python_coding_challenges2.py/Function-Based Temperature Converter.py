# Function-Based Temperature Converter

temperatures = [25, 30, 35, 40, 28, 32, 38, 22, 27, 31]

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# Function to display all temperatures in Fahrenheit
def display_fahrenheit(temp_list):
    fahrenheit_list = []

    print("Temperatures in Fahrenheit:")
    for temp in temp_list:
        f = celsius_to_fahrenheit(temp)
        fahrenheit_list.append(f)
        print(f)

    return fahrenheit_list

# Main Program
fahrenheit_temperatures = display_fahrenheit(temperatures)

# Highest Fahrenheit temperature
highest = max(fahrenheit_temperatures)

# Lowest Fahrenheit temperature
lowest = min(fahrenheit_temperatures)

# Average Fahrenheit temperature
average = sum(fahrenheit_temperatures) / len(fahrenheit_temperatures)

print("\nHighest Temperature:", highest, "°F")
print("Lowest Temperature:", lowest, "°F")
print("Average Temperature:", round(average, 2), "°F")