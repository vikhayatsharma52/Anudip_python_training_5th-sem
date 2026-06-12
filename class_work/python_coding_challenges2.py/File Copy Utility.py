# File Copy Utility

# Read source file
source_file = open("notes.txt", "r")
data = source_file.read()
source_file.close()

# Copy content to backup file
backup_file = open("backup.txt", "w")
backup_file.write(data)
backup_file.close()

print("File copied successfully.")

# Verify number of lines
source_file = open("notes.txt", "r")
source_lines = len(source_file.readlines())
source_file.close()

backup_file = open("backup.txt", "r")
backup_lines = len(backup_file.readlines())
backup_file.close()

print("\nSource File Lines:", source_lines)
print("\nBackup File Lines:", backup_lines)

if source_lines == backup_lines:
    print("\nVerification Status: Successful")
else:
    print("\nVerification Status: Failed")