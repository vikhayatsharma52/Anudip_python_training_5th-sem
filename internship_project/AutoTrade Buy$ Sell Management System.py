# ==========================================================

# AUTOTRADE BUY & SELL MANAGEMENT SYSTEM

# ==========================================================

# Features:
# 1. Add Tractor
# 2. View All Tractors
# 3. Search Tractor
# 4. Update Tractor
# 5. Delete Tractor
# 6. Show Companies
# 7. Total Tractors
# 8. Buy Tractor
# 9. Exit
#
# Concepts Used:
# List, Tuple, Set, Dictionary, Functions,
# Loops, Exception Handling, Conditional Statements
# ==========================================================

# Dictionary to store tractor records
tractors = {}

# List to store tractor IDs
tractor_ids = []

# Set to store unique company names
companies = set()


# ----------------------------------------------------------
# Function to rebuild company set after delete/buy operation
# ----------------------------------------------------------
def update_companies():
    companies.clear()

    for data in tractors.values():
        companies.add(data[0])  # Company Name


# ----------------------------------------------------------
# Function to add a new tractor
# ----------------------------------------------------------
def add_tractor():

    tractor_id = input("Enter Tractor ID: ")

    if tractor_id in tractors:
        print("Tractor ID Already Exists!")
        return

    company = input("Enter Company Name: ")
    model = input("Enter Model Name: ")

    # Input validation for year
    while True:
        try:
            year = int(input("Enter Manufacturing Year: "))
            break
        except ValueError:
            print("Please enter a valid year!")

    # Input validation for price
    while True:
        try:
            price = float(input("Enter Price: "))
            break
        except ValueError:
            print("Please enter a valid price!")

    owner = input("Enter Owner Name: ")
    mobile = input("Enter Mobile Number: ")
    condition = input("Enter Condition (Good/Average/Excellent): ")
    location = input("Enter Location: ")

    # Tuple to store tractor details
    tractor_data = (
        company,
        model,
        year,
        price,
        owner,
        mobile,
        condition,
        location
    )

    # Store data in dictionary
    tractors[tractor_id] = tractor_data

    # Add tractor ID into list
    tractor_ids.append(tractor_id)

    # Add company into set
    companies.add(company)

    print("Tractor Added Successfully!")


# ----------------------------------------------------------
# Function to view all tractors
# ----------------------------------------------------------
def view_tractors():

    if len(tractors) == 0:
        print("No Tractors Available!")
        return

    print("\n========== AVAILABLE TRACTORS ==========")

    for tractor_id in tractor_ids:

        if tractor_id in tractors:

            company, model, year, price, owner, mobile, condition, location = tractors[tractor_id]

            print("\n--------------------------------")
            print("Tractor ID :", tractor_id)
            print("Company    :", company)
            print("Model      :", model)
            print("Year       :", year)
            print("Price      :", price)
            print("Owner      :", owner)
            print("Mobile     :", mobile)
            print("Condition  :", condition)
            print("Location   :", location)


# ----------------------------------------------------------
# Function to search tractor by ID
# ----------------------------------------------------------
def search_tractor():

    tractor_id = input("Enter Tractor ID: ")

    if tractor_id in tractors:

        company, model, year, price, owner, mobile, condition, location = tractors[tractor_id]

        print("\nTractor Found!")
        print("Company   :", company)
        print("Model     :", model)
        print("Year      :", year)
        print("Price     :", price)
        print("Owner     :", owner)
        print("Mobile    :", mobile)
        print("Condition :", condition)
        print("Location  :", location)

    else:
        print("Tractor Not Found!")


# ----------------------------------------------------------
# Function to update tractor details
# ----------------------------------------------------------
def update_tractor():

    tractor_id = input("Enter Tractor ID To Update: ")

    if tractor_id not in tractors:
        print("Tractor Not Found!")
        return

    company, model, year, price, owner, mobile, condition, location = tractors[tractor_id]

    print("\nLeave blank if you don't want to change a value.")

    new_price = input(f"New Price ({price}): ")
    new_condition = input(f"New Condition ({condition}): ")

    if new_price != "":
        try:
            price = float(new_price)
        except ValueError:
            print("Invalid Price!")
            return

    if new_condition != "":
        condition = new_condition

    tractors[tractor_id] = (
        company,
        model,
        year,
        price,
        owner,
        mobile,
        condition,
        location
    )

    print("Tractor Updated Successfully!")


# ----------------------------------------------------------
# Function to delete tractor
# ----------------------------------------------------------
def delete_tractor():

    tractor_id = input("Enter Tractor ID To Delete: ")

    if tractor_id in tractors:

        del tractors[tractor_id]

        if tractor_id in tractor_ids:
            tractor_ids.remove(tractor_id)

        update_companies()

        print("Tractor Deleted Successfully!")

    else:
        print("Tractor Not Found!")


# ----------------------------------------------------------
# Function to show companies
# ----------------------------------------------------------
def show_companies():

    if len(companies) == 0:
        print("No Companies Available!")
        return

    print("\n========== COMPANIES ==========")

    for company in companies:
        print(company)


# ----------------------------------------------------------
# Function to count total tractors
# ----------------------------------------------------------
def total_tractors():
    print("Total Tractors Available:", len(tractors))


# ----------------------------------------------------------
# Function to buy tractor
# ----------------------------------------------------------
def buy_tractor():

    tractor_id = input("Enter Tractor ID To Buy: ")

    if tractor_id in tractors:

        del tractors[tractor_id]

        if tractor_id in tractor_ids:
            tractor_ids.remove(tractor_id)

        update_companies()

        print("Congratulations!")
        print("Tractor Purchased Successfully!")

    else:
        print("Tractor Not Available!")


# ==========================================================
# MAIN MENU
# ==========================================================

while True:

    print("\n====================================")
    print(" AUTOTRADE BUY & SELL MANAGEMENT SYSTEM ")
    print("====================================")
    print("1. Add Tractor")
    print("2. View All Tractors")
    print("3. Search Tractor")
    print("4. Update Tractor")
    print("5. Delete Tractor")
    print("6. Show Companies")
    print("7. Total Tractors")
    print("8. Buy Tractor")
    print("9. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_tractor()

    elif choice == "2":
        view_tractors()

    elif choice == "3":
        search_tractor()

    elif choice == "4":
        update_tractor()

    elif choice == "5":
        delete_tractor()

    elif choice == "6":
        show_companies()

    elif choice == "7":
        total_tractors()

    elif choice == "8":
        buy_tractor()

    elif choice == "9":
        print("Thank You For Using The System!")
        break

    else:
        print("Invalid Choice! Please Enter Between 1 and 9.") 