#9. Mobile Contact Directory
S#ample Data
c##ontacts = {
 #"Amit": "9876543210",
 ##"Priya": "9876543211",
 #"Rohan": "9876543212",
 #"Neha": "9876543213",
 #"Anjali": "9876543214",
 #"Karan": "9876543215",
 #"Pooja": "9876543216",
 #3"Arjun": "9876543217",
 #3"Sneha": "9876543218",
 #"Rahul": "9876543219"
#}
#Tasks
#• Display all contact names in alphabetical order.
#• Count the total number of contacts.
##• Search for a given contact name.
#• Create a list of contacts whose names start with a vowel.
#• Stop the search using break once the required contact is found. 

contacts = {
    "Amit": "9876543210",
    "Priya": "9876543211",
    "Rohan": "9876543212",
    "Neha": "9876543213",
    "Anjali": "9876543214",
    "Karan": "9876543215",
    "Pooja": "9876543216",
    "Arjun": "9876543217",
    "Sneha": "9876543218",
    "Rahul": "9876543219"
}

# Display all contact names in alphabetical order
print("Contact Names in Alphabetical Order:")
for name in sorted(contacts):
    print(name)

# Count the total number of contacts
print("\nTotal Contacts:", len(contacts))

# Search for a given contact name using break
search_name = input("\nEnter contact name to search: ")

found = False
for name, number in contacts.items():
    if name.lower() == search_name.lower():
        print("Contact Found:")
        print(name, "-", number)
        found = True
        break

if not found:
    print("Contact Not Found")

# Create a list of contacts whose names start with a vowel
vowel_contacts = []

for name in contacts:
    if name[0].lower() in ['a', 'e', 'i', 'o', 'u']:
        vowel_contacts.append(name)

print("\nContacts Starting with a Vowel:")
print(vowel_contacts)