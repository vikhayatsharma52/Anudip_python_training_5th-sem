reviews = [
    "excellent movie",
    "average story",
    "excellent acting",
    "poor direction",
    "excellent visuals",
    "poor screenplay",
    "good music",
    "excellent climax",
    "average performance",
    "good cinematography"
]

# 1. Count sentiments
def count_sentiments(reviews):
    excellent = 0
    good = 0
    average = 0
    poor = 0

    for review in reviews:
        if review.startswith("excellent"):
            excellent += 1
        elif review.startswith("good"):
            good += 1
        elif review.startswith("average"):
            average += 1
        elif review.startswith("poor"):
            poor += 1

    print("Excellent Reviews:", excellent)
    print("Good Reviews:", good)
    print("Average Reviews:", average)
    print("Poor Reviews:", poor)


# 2. Most common word
def most_common_word(reviews):
    words = {}

    for review in reviews:
        for word in review.split():
            if word in words:
                words[word] += 1
            else:
                words[word] = 1

    max_word = max(words, key=words.get)
    return max_word


# 3. Longest review
def longest_review(reviews):
    longest = reviews[0]

    for review in reviews:
        if len(review) > len(longest):
            longest = review

    return longest


# 4. Reviews with keyword
def reviews_with_keyword(reviews, keyword):
    for review in reviews:
        if keyword in review:
            print(review)


# Function Calls
count_sentiments(reviews)

print("\nMost Common Word:")
print(most_common_word(reviews))

print("\nLongest Review:")
print(longest_review(reviews))

print("\nReviews containing 'excellent':")
reviews_with_keyword(reviews, "excellent") 