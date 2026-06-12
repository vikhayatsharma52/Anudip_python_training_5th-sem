# Movie Rating Analysis System

ratings = {
    "Inception": 4.8,
    "Avatar": 4.3,
    "Titanic": 4.5,
    "Joker": 4.7,
    "Frozen": 3.8,
    "Interstellar": 4.9,
    "Dune": 4.6,
    "Up": 4.1,
    "Coco": 4.4,
    "Cars": 3.9
}

# 1. Display movies rated above 4.5
print("Movies Rated Above 4.5:")
for movie, rating in ratings.items():
    if rating > 4.5:
        print(movie)

# 2. Find the highest-rated movie
highest_movie = max(ratings, key=ratings.get)
print("\nHighest Rated Movie:")
print(highest_movie, "(", ratings[highest_movie], ")", sep="")

# 3. Find the lowest-rated movie
lowest_movie = min(ratings, key=ratings.get)
print("\nLowest Rated Movie:")
print(lowest_movie, "(", ratings[lowest_movie], ")", sep="")

# 4. Calculate average rating
average = sum(ratings.values()) / len(ratings)
print("\nAverage Rating:", round(average, 1))

# 5. Create recommendation list (rating >= 4.5)
recommended = []

for movie, rating in ratings.items():
    if rating >= 4.5:
        recommended.append(movie)

print("\nRecommended Movies:")
print(recommended)