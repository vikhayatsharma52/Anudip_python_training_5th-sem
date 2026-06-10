# Mobile Contact Directory System

while True:

    print("\n===== Contact Directory =====")
    print("1. Display All Contacts")
    print("2. Search Contact")
    print("3. Add New Contact")
    print("4. Update Contact Number")
    print("5. Delete Contact")
    print("6. Contacts Starting With Vowel")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    # 1. Display all contacts
    if choice == 1:

        f = open("contacts.txt", "r")

        print("\nContacts List:")
        for line in f:
            print(line.strip())

        f.close()

    # 2. Search contact by name
    elif choice == 2:

        name = input("Enter Name: ")

        f = open("contacts.txt", "r")
        found = False

        for line in f:

            data = line.strip().split(",")

            if data[0].lower() == name.lower():

                print("Name =", data[0])
                print("Number =", data[1])

                found = True

        if found == False:
            print("Contact Not Found")

        f.close()

    # 3. Add new contact
    elif choice == 3:

        name = input("Enter Name: ")
        number = input("Enter Number: ")

        f = open("contacts.txt", "a")
        f.write("\n" + name + "," + number)
        f.close()

        print("Contact Added Successfully")

    # 4. Update contact number
    elif choice == 4:

        name = input("Enter Name to Update: ")

        f = open("contacts.txt", "r")

        contacts = []
        found = False

        for line in f:

            data = line.strip().split(",")

            if data[0].lower() == name.lower():

                new_number = input("Enter New Number: ")

                data[1] = new_number
                found = True

            contacts.append(",".join(data))

        f.close()

        f = open("contacts.txt", "w")

        for contact in contacts:
            f.write(contact + "\n")

        f.close()

        if found:
            print("Contact Updated Successfully")
        else:
            print("Contact Not Found")

    # 5. Delete contact
    elif choice == 5:

        name = input("Enter Name to Delete: ")

        f = open("contacts.txt", "r")

        contacts = []
        found = False

        for line in f:

            data = line.strip().split(",")

            if data[0].lower() == name.lower():
                found = True
            else:
                contacts.append(",".join(data))

        f.close()

        f = open("contacts.txt", "w")

        for contact in contacts:
            f.write(contact + "\n")

        f.close()

        if found:
            print("Contact Deleted Successfully")
        else:
            print("Contact Not Found")

    # 6. Contacts starting with vowel
    elif choice == 6:

        f = open("contacts.txt", "r")

        print("\nContacts Starting With Vowel:")

        for line in f:

            data = line.strip().split(",")

            if data[0][0].lower() in "aeiou":
                print(data[0], data[1])

        f.close()

    # 7. Exit
    elif choice == 7:

        print("Program Ended")
        break

    else:
        print("Invalid Choice")