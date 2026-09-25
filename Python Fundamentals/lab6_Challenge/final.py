# Final challenge - Tournament report

# Cleaned data from Part 2
players = [
    {"name": "Sarah", "team": "Red", "country": "SE", "score": 100, "matches": 5, "wins": 3, "active": True},
    {"name": "Ada", "team": "Blue", "country": "SE", "score": 80, "matches": 4, "wins": 1, "active": False},
    {"name": "Abel", "team": "Red", "country": "ETH", "score": 120, "matches": 6, "wins": 4, "active": True},
    {"name": "Isac", "team": "Blue", "country": "ETH", "score": 90, "matches": 4, "wins": 2, "active": True},
    {"name": "Mike", "team": "Green", "country": "UK", "score": 75, "matches": 5, "wins": 0, "active": False},
    {"name": "David", "team": "Green", "country": "UK", "score": 110, "matches": 5, "wins": 3, "active": True},
    {"name": "Adam", "team": "Red", "country": "SE", "score": 130, "matches": 6, "wins": 5, "active": True},
    {"name": "Johone", "team": "Blue", "country": "USA", "score": 95, "matches": 4, "wins": 2, "active": True},
    {"name": "Lina", "team": "Green", "country": "USA", "score": 115, "matches": 5, "wins": 4, "active": True},
    {"name": "Yusuf", "team": "Red", "country": "ETH", "score": 85, "matches": 5, "wins": 1, "active": False},
    {"name": "Ruth", "team": "Blue", "country": "ETH", "score": 105, "matches": 4, "wins": 3, "active": True},
    {"name": "Paul", "team": "Green", "country": "UK", "score": 70, "matches": 3, "wins": 0, "active": True},
    {"name": "Maya", "team": "Red", "country": "USA", "score": 140, "matches": 6, "wins": 6, "active": True},
    {"name": "James", "team": "Blue", "country": "UK", "score": 65, "matches": 4, "wins": 1, "active": False},
    {"name": "Tina", "team": "Green", "country": "SE", "score": 125, "matches": 5, "wins": 4, "active": True},
]

active = [player for player in players if player["active"]]
teams = {player["team"] for player in players}
countries = {player["country"] for player in players}
by_score = sorted(players, key=lambda player: player["score"], reverse=True)
by_wins = sorted(players, key=lambda player: player["wins"], reverse=True)
performance = {player["name"]: player["score"] + player["wins"] * 10 for player in players}
high_performance = {name: points for name, points in performance.items() if points > 130}


no_wins = [player["name"] for player in players if player["wins"] == 0]
inactive = [player["name"] for player in players if not player["active"]]
scores = [player["score"] for player in players]

print("Total players:", len(players))
print("Active players:", len(active))
print("Teams:", teams)
print("Countries:", countries)
print("Score ranking:")
for rank, player in enumerate(by_score, start=1):
    print(rank, player["name"], player["score"])
print("Wins ranking:")
for rank, player in enumerate(by_wins, start=1):
    print(rank, player["name"], player["wins"])
print("Top 5:", [player["name"] for player in by_score[:5]])
print("Performance above 130:", high_performance)
print("No wins:", no_wins)
print("Inactive players:", inactive)
print("Average score:", sum(scores) / len(scores))

# Design exercise: combining several steps in one comprehension is hard to read.
complicated = [
    player["name"].upper()
    for player in sorted(players, key=lambda player: player["score"], reverse=True)
    if player["active"] if player["score"] > 100
]

# Reuse the ranking and separate the condition from formatting the name.
simple = []
for player in by_score:
    if player["active"] and player["score"] > 100:
        simple.append(player["name"].upper())
print("Active high scorers:", simple)
