# Part 6 - Four rankings

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

# lambda selects the value to sort by. reverse=True puts the largest first.
by_score = sorted(players, key=lambda player: player["score"], reverse=True)
by_wins = sorted(players, key=lambda player: player["wins"], reverse=True)
by_matches = sorted(players, key=lambda player: player["matches"], reverse=True)
by_name = sorted(players, key=lambda player: player["name"])

print("Highest score first:")
for player in by_score:
    print(player["name"], player["score"])

print("Most wins first:")
for player in by_wins:
    print(player["name"], player["wins"])

print("Most matches first:")
for player in by_matches:
    print(player["name"], player["matches"])

print("Alphabetical order:")
for player in by_name:
    print(player["name"])
# sorted creates a new list, so players stays in its original order.
