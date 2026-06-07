#4. Cricket Scoreboard Analysis
#Sample Data
#scores = {
## "Virat": 78,
## "Rohit": 112,
 ##"Gill": 45,
 #"Rahul": 89,
 #"Hardik": 32,
 #"Jadeja": 61,
# "Surya": 105,
# "Pant": 95,
# "Bumrah": 18,
# "Shami": 25
#}
#Tasks
# Display players who scored 50 or more runs.
# Count the number of centuries.
#• Find the player with the highest score.
#• Create a list of players scoring below 30 runs.
#• Determine how many players scored between 50 and 99. 


scores = {
    "Virat": 78,
    "Rohit": 112,
    "Gill": 45,
    "Rahul": 89,
    "Hardik": 32,
    "Jadeja": 61,
    "Surya": 105,
    "Pant": 95,
    "Bumrah": 18,
    "Shami": 25
}

# Players who scored 50 or more runs
print("Players who scored 50 or more runs:")
for player, runs in scores.items():
    if runs >= 50:
        print(player, "-", runs)

# Count the number of centuries
centuries = 0
for runs in scores.values():
    if runs >= 100:
        centuries += 1

print("\nNumber of centuries:", centuries)

# Find the player with the highest score
highest_player = max(scores, key=scores.get)
print("\nPlayer with highest score:")
print(highest_player, "-", scores[highest_player])

# Create a list of players scoring below 30 runs
below_30 = []
for player, runs in scores.items():
    if runs < 30:
        below_30.append(player)

print("\nPlayers scoring below 30 runs:")
print(below_30)

# Count players scoring between 50 and 99
count = 0
for runs in scores.values():
    if 50 <= runs <= 99:
        count += 1

print("\nPlayers scoring between 50 and 99:", count)