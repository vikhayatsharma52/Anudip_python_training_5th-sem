# Word Frequency Analyzer

file = open("article.txt", "r")

text = file.read().lower()
file.close()

# Remove punctuation
text = text.replace(".", "")

# Convert text into words
words = text.split()

# 1. Count total number of words
total_words = len(words)

# 2. Count frequency of each word
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

# 3. Find most frequently occurring word
most_word = max(frequency, key=frequency.get)

# 4. Find words appearing only once
once_words = []

for word, count in frequency.items():
    if count == 1:
        once_words.append(word)

# 5. Find all unique words
unique_words = list(frequency.keys())

# Display Results
print("Total Words:", total_words)

print("\nMost Frequent Word:")
print(most_word, "(", frequency[most_word], "times)", sep=" ")

print("\nWords Appearing Once:")
for word in once_words:
    print(word)

print("\nUnique Words Count:", len(unique_words))