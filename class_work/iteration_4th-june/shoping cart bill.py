total = 0

while True:
    #enter the price
    price = float(input("Enter item price (0 to stop): "))

    if price == 0:
        break

    total += price
#................................
print("Total Bill Amount =", total)