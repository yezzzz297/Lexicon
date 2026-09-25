# Part 5 - Combine lists with zip()

names = ["Sarah", "Ada", "Abel"]
scores = [100, 80, 120]
teams = ["Red", "Blue", "Red"]

# Example 1: names and scores.
print("Player scores:")
for name, score in zip(names, scores):
    print(name, score)

# Example 2: names and teams.
print("Player teams:")
for name, team in zip(names, teams):
    print(name, team)

# Example 3: three lists together.
print("Players, teams and scores:")
for name, team, score in zip(names, teams, scores):
    print(name, team, score)

short_scores = [100, 80]
print("Different lengths:")
for name, score in zip(names, short_scores):
    print(name, score)
# zip stops at the shorter list, so Abel has no pair here.
