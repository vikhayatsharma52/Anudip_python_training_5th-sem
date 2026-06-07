#5. Library Book Availability
#Sample Data
#books = {
# "Python Basics": 5,
# "Data Structures": 0,
# "Machine Learning": 3,
# "Java Programming": 2,
# "DBMS": 0,
# "Operating Systems": 6,
# "Networking": 4,
# "Cloud Computing": 1,
# "Cyber Security": 0,
# "Web Development": 7
#}
#Tasks
#• Display books that are currently unavailable.
#• Count the number of available books.
#• Find the book with the maximum copies.
#• Create a list of books having less than 3 copies.




books = {
    "Python Basics": 5,
    "Data Structures": 0,
    "Machine Learning": 3,
    "Java Programming": 2,
    "DBMS": 0,
    "Operating Systems": 6,
    "Networking": 4,
    "Cloud Computing": 1,
    "Cyber Security": 0,
    "Web Development": 7
}

# Display books that are currently unavailable
print("Unavailable Books:")
for book, copies in books.items():
    if copies == 0:
        print(book)

# Count the number of available books
count = 0
for copies in books.values():
    if copies > 0:
        count += 1

print("\nNumber of Available Books:", count)

# Find the book with the maximum copies
max_book = max(books, key=books.get)
print("\nBook with Maximum Copies:")
print(max_book, "-", books[max_book])

# Create a list of books having less than 3 copies
less_than_3 = []
for book, copies in books.items():
    if copies < 3:
        less_than_3.append(book)

print("\nBooks Having Less Than 3 Copies:")
print(less_than_3)

# Calculate the total number of books available
total = 0
for copies in books.values():
    total += copies

print("\nTotal Number of Books Available:", total)

