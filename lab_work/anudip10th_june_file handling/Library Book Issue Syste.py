while True:
    print("\n===== Library Book Issue System =====")
    print("1. Display All Books")
    print("2. Search Book by ID")
    print("3. Issue a Book")
    print("4. Return a Book")
    print("5. Display Unavailable Books")
    print("6. Display Books Requiring Restocking")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        f = open("books.txt", "r")

        print("\nBook Records:")
        for line in f:
            print(line.strip())

        f.close()

    elif choice == 2:
        book_id = input("Enter Book ID: ")

        f = open("books.txt", "r")
        found = False

        for line in f:
            data = line.strip().split(",")

            if data[0] == book_id:
                print("Book ID:", data[0])
                print("Book Name:", data[1])
                print("Quantity:", data[2])
                found = True

        if found == False:
            print("Book not found")

        f.close()

    elif choice == 3:
        book_id = input("Enter Book ID to Issue: ")

        f = open("books.txt", "r")
        books = []

        for line in f:
            data = line.strip().split(",")

            if data[0] == book_id:
                qty = int(data[2])

                if qty > 0:
                    qty = qty - 1
                    data[2] = str(qty)
                    print("Book Issued Successfully")
                else:
                    print("Book Not Available")

            books.append(",".join(data))

        f.close()

        f = open("books.txt", "w")
        for book in books:
            f.write(book + "\n")
        f.close()

    elif choice == 4:
        book_id = input("Enter Book ID to Return: ")

        f = open("books.txt", "r")
        books = []

        for line in f:
            data = line.strip().split(",")

            if data[0] == book_id:
                qty = int(data[2]) + 1
                data[2] = str(qty)
                print("Book Returned Successfully")

            books.append(",".join(data))

        f.close()

        f = open("books.txt", "w")
        for book in books:
            f.write(book + "\n")
        f.close()

    elif choice == 5:
        f = open("books.txt", "r")

        print("\nUnavailable Books:")

        for line in f:
            data = line.strip().split(",")

            if int(data[2]) == 0:
                print(data[0], data[1])

        f.close()

    elif choice == 6:
        f = open("books.txt", "r")

        print("\nBooks Requiring Restocking:")

        for line in f:
            data = line.strip().split(",")

            if int(data[2]) < 2:
                print(data[0], data[1], data[2])

        f.close()

    elif choice == 7:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")