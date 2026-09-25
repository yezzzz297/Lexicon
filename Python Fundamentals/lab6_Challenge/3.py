# Part 3 - Five filters

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

# Each list contains the names that match one condition.
active = [player["name"] for player in players if player["active"]]
three_wins = [player["name"] for player in players if player["wins"] >= 3]
high_scores = [player["name"] for player in players if player["score"] > 100]
from_sweden = [player["name"] for player in players if player["country"] == "SE"]
active_high = [
    player["name"] for player in players
    if player["active"] and player["score"] > 100
]

print("Active players:", active)
print("At least 3 wins:", three_wins)
print("Score above 100:", high_scores)
print("From Sweden:", from_sweden)
print("Active and above 100:", active_high)
