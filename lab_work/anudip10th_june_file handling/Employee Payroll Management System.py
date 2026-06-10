while True:
    print("\n----- Employee Payroll Management System -----")
    print("1. Display all employee records")
    print("2. Search employee by ID")
    print("3. Calculate average salary")
    print("4. Highest and Lowest paid employee")
    print("5. Employees earning above 50000")
    print("6. Add new employee")
    print("7. Salary categories")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        f = open("employees.txt", "r")

        print("\nEmployee Records:")
        for line in f:
            print(line.strip())

        f.close()

    elif choice == 2:
        emp_id = input("Enter Employee ID: ")

        f = open("employees.txt", "r")
        found = False

        for line in f:
            data = line.strip().split(",")

            if data[0] == emp_id:
                print("ID:", data[0])
                print("Name:", data[1])
                print("Salary:", data[2])
                found = True

        if found == False:
            print("Employee not found")

        f.close()

    elif choice == 3:
        f = open("employees.txt", "r")

        total = 0
        count = 0

        for line in f:
            data = line.strip().split(",")
            total += int(data[2])
            count += 1

        avg = total / count
        print("Average Salary =", avg)

        f.close()

    elif choice == 4:
        f = open("employees.txt", "r")

        employees = []

        for line in f:
            data = line.strip().split(",")
            employees.append(data)

        highest = employees[0]
        lowest = employees[0]

        for emp in employees:
            if int(emp[2]) > int(highest[2]):
                highest = emp

            if int(emp[2]) < int(lowest[2]):
                lowest = emp

        print("Highest Paid Employee:")
        print(highest[0], highest[1], highest[2])

        print("Lowest Paid Employee:")
        print(lowest[0], lowest[1], lowest[2])

        f.close()

    elif choice == 5:
        f = open("employees.txt", "r")

        print("Employees earning above 50000:")

        for line in f:
            data = line.strip().split(",")

            if int(data[2]) > 50000:
                print(data[0], data[1], data[2])

        f.close()

    elif choice == 6:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        salary = input("Enter Salary: ")

        f = open("employees.txt", "a")
        f.write("\n" + emp_id + "," + name + "," + salary)
        f.close()

        print("Employee Added Successfully")

    elif choice == 7:
        f = open("employees.txt", "r")

        for line in f:
            data = line.strip().split(",")

            salary = int(data[2])

            if salary >= 60000:
                category = "High"
            elif salary >= 40000:
                category = "Medium"
            else:
                category = "Low"

            print(data[1], "-", category)

        f.close()

    elif choice == 8:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")