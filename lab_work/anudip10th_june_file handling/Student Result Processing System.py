# Student Result Processing System

while True:

    # Display Menu
    print("\n===== Student Result Processing System =====")
    print("1. Display all student records")
    print("2. Search student by ID")
    print("3. Find topper and lowest scorer")
    print("4. Calculate class average")
    print("5. Count pass and fail students")
    print("6. Generate grades")
    print("7. Create grades.txt file")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    # 1. Display all records
    if choice == 1:

        f = open("results.txt", "r")

        print("\nStudent Records:")
        for line in f:
            print(line.strip())

        f.close()

    # 2. Search Student
    elif choice == 2:

        sid = input("Enter Student ID: ")

        f = open("results.txt", "r")
        found = False

        for line in f:

            data = line.strip().split(",")

            if data[0] == sid:
                print("ID =", data[0])
                print("Name =", data[1])
                print("Marks =", data[2])

                found = True

        if found == False:
            print("Student Not Found")

        f.close()

    # 3. Topper and Lowest Scorer
    elif choice == 3:

        f = open("results.txt", "r")

        students = []

        for line in f:
            data = line.strip().split(",")
            students.append(data)

        topper = students[0]
        lowest = students[0]

        for s in students:

            if int(s[2]) > int(topper[2]):
                topper = s

            if int(s[2]) < int(lowest[2]):
                lowest = s

        print("\nTopper:")
        print(topper[0], topper[1], topper[2])

        print("\nLowest Scorer:")
        print(lowest[0], lowest[1], lowest[2])

        f.close()

    # 4. Calculate Average
    elif choice == 4:

        f = open("results.txt", "r")

        total = 0
        count = 0

        for line in f:

            data = line.strip().split(",")

            total = total + int(data[2])
            count = count + 1

        average = total / count

        print("Class Average =", average)

        f.close()

    # 5. Count Pass and Fail
    elif choice == 5:

        f = open("results.txt", "r")

        pass_count = 0
        fail_count = 0

        for line in f:

            data = line.strip().split(",")

            marks = int(data[2])

            if marks >= 40:
                pass_count += 1
            else:
                fail_count += 1

        print("Pass Students =", pass_count)
        print("Fail Students =", fail_count)

        f.close()

    # 6. Generate Grades
    elif choice == 6:

        f = open("results.txt", "r")

        print("\nGrade Report")

        for line in f:

            data = line.strip().split(",")

            marks = int(data[2])

            if marks >= 90:
                grade = "A"
            elif marks >= 75:
                grade = "B"
            elif marks >= 40:
                grade = "C"
            else:
                grade = "F"

            print(data[1], "-", grade)

        f.close()

    # 7. Create grades.txt
    elif choice == 7:

        f = open("results.txt", "r")
        g = open("grades.txt", "w")

        for line in f:

            data = line.strip().split(",")

            marks = int(data[2])

            if marks >= 90:
                grade = "A"
            elif marks >= 75:
                grade = "B"
            elif marks >= 40:
                grade = "C"
            else:
                grade = "F"

            g.write(data[0] + "," + data[1] + "," + grade + "\n")

        f.close()
        g.close()

        print("grades.txt file created successfully")

    # 8. Exit
    elif choice == 8:

        print("Program Ended")
        break

    else:
        print("Invalid Choice")