# Library books
books = [
    ("Python Basics", 5),
    ("Data Science", 0),
    ("Java Programming", 3),
    ("Machine Learning", 0)
]

# Display unavailable books
print("Unavailable Books:")

for book in books:
    if book[1] == 0:          # Check copies
        print(book[0])

# Find books with more than 2 copies
print("\nBooks With More Than 2 Copies:")

for book in books:
    if book[1] > 2:
        print(book[0])

# Count available books
count = 0

for book in books:
    if book[1] > 0:           # Available copies
        count += 1

print("\nAvailable Books:", count)

# Search a book and stop when found
search = "Java Programming"

for book in books:
    if book[0] == search:     # Check book name
        print("\nBook Found:", book[0])
        break                 # Stop searching