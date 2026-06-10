# File Content Analyzer

# File ko read mode me open karna
f = open("article.txt", "r")

# Puri file ka data read karna
data = f.read()

# Vowels count karne ke liye variable
vowels = 0

# File ke har character par loop chalana
for ch in data:

    # Agar character vowel hai to count badhao
    if ch.lower() in "aeiou":
        vowels += 1

# Total characters count karna
# (spaces aur special characters bhi include honge)
characters = len(data)

# Total lines count karna
# Har new line (\n) ko count karke +1 karte hain
lines = data.count("\n") + 1

# Report display karna
print("File Analysis Report")
print()

print("Total Number of Vowels    :", vowels)
print("Total Number of Characters:", characters)
print("Total Number of Lines     :", lines)

# File close karna
f.close()