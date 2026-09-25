# Part 4 - Sets and dictionaries

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

countries = {player["country"] for player in players}
teams = {player["team"] for player in players}
scores = {player["name"]: player["score"] for player in players}
wins = {player["name"]: player["wins"] for player in players}
high_scores = {player["name"]: player["score"] for player in players if player["score"] >= 100}

print("Countries:", countries)
print("Teams:", teams)
print("Scores:", scores)
print("Wins:", wins)
print("Scores of at least 100:", high_scores)
# A set comprehension replaces a loop adding each country; duplicates disappear.
# A dictionary comprehension replaces a loop assigning each name and score.
