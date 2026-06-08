runs = {
    "Virat": 645,
    "Rohit": 512,
    "Gill": 698,
    "Rahul": 435,
    "Hardik": 278,
    "Pant": 534,
    "Surya": 389,
    "Jadeja": 301,
    "Iyer": 455,
    "KL": 410
}

# 1. Display players scoring more than 500 runs
print("Players Scoring More Than 500 Runs:")
for player, score in runs.items():
    if score > 500:
        print(player)

# 2. Find the Orange Cap winner
orange_cap = max(runs, key=runs.get)
print("\nOrange Cap Winner:", orange_cap, f"({runs[orange_cap]})")

# 3. Find the lowest scorer
lowest_scorer = min(runs, key=runs.get)
print("\nLowest Scorer:", lowest_scorer, f"({runs[lowest_scorer]})")

# 4. Calculate total runs scored
total_runs = sum(runs.values())
print("\nTotal Tournament Runs:", total_runs)

# 5. Create a list of players scoring below 400
below_400 = [player for player, score in runs.items() if score < 400]
print("\nPlayers Scoring Below 400:")
print(below_400)

# 6. Count players scoring between 400 and 600 runs
count_players = sum(1 for score in runs.values() if 400 <= score <= 600)
print("\nPlayers Between 400 and 600 Runs:", count_players)