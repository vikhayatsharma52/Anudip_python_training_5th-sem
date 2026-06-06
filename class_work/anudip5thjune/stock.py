# Inventory Stock Alert System

stock = [25, 5, 0, 12, 3, 18, 0, 30]

# counters and lists
out_of_stock = 0
available_products = 0
restock = []
healthy_stock = []

# check all stock values
for qty in stock:

    # count out of stock products
    if qty == 0:
        out_of_stock += 1

    # count available products
    if qty > 0:
        available_products += 1

    # products needing restock
    if qty < 10:
        restock.append(qty)

    # healthy stock products
    if qty >= 15:
        healthy_stock.append(qty)

# display results
print("Out of Stock Products:", out_of_stock)
print("Restock Required:", restock)
print("Available Products:", available_products)
print("Healthy Stock:", healthy_stock)