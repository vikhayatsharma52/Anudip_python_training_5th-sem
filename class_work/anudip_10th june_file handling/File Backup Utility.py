# File Backup Utility

# Input source file name
source_file = input("Enter Source File Name : ")

# Input destination file name
destination_file = input("Enter Destination File Name : ")

# Open source file in read mode
f1 = open(source_file, "r")

# Read all data from source file
data = f1.read()

# Close source file
f1.close()

# Open destination file in write mode
f2 = open(destination_file, "w")

# Write data into destination file
f2.write(data)

# Close destination file
f2.close()

# Display success message
print("\nFile copied successfully.")
print("All contents from", source_file, "have been copied to", destination_file)