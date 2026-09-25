# Part 2 - Clean the data without changing the original

players = [
    {"name": "  sarah  ", "team": "Red", "country": "se", "score": 100, "matches": 5, "wins": 3, "active": True},
    {"name": "ADA", "team": "Blue", "country": "SE", "score": 80, "matches": 4, "wins": 1, "active": False},
    {"name": "abel", "team": "Red", "country": "eth", "score": 120, "matches": 6, "wins": 4, "active": True},
    {"name": "Isac", "team": "Blue", "country": "ETH", "score": 90, "matches": 4, "wins": 2, "active": True},
    {"name": "mike ", "team": "Green", "country": "uk", "score": 75, "matches": 5, "wins": 0, "active": False},
    {"name": "DAVID", "team": "Green", "country": "UK", "score": 110, "matches": 5, "wins": 3, "active": True},
    {"name": "Adam", "team": "Red", "country": "se", "score": 130, "matches": 6, "wins": 5, "active": True},
    {"name": "Johone", "team": "Blue", "country": "usa", "score": 95, "matches": 4, "wins": 2, "active": True},
    {"name": "Lina", "team": "Green", "country": "USA", "score": 115, "matches": 5, "wins": 4, "active": True},
    {"name": "Yusuf", "team": "Red", "country": "eth", "score": 85, "matches": 5, "wins": 1, "active": False},
    {"name": "Ruth", "team": "Blue", "country": "ETH", "score": 105, "matches": 4, "wins": 3, "active": True},
    {"name": "Paul", "team": "Green", "country": "uk", "score": 70, "matches": 3, "wins": 0, "active": True},
    {"name": "Maya", "team": "Red", "country": "usa", "score": 140, "matches": 6, "wins": 6, "active": True},
    {"name": "James", "team": "Blue", "country": "UK", "score": 65, "matches": 4, "wins": 1, "active": False},
    {"name": "Tina", "team": "Green", "country": "se", "score": 125, "matches": 5, "wins": 4, "active": True},
]

# Copy each dictionary so cleaning does not change the original players.
cleaned_players = [player.copy() for player in players]

for player in cleaned_players:
    player["name"] = player["name"].strip().title()
    player["team"] = player["team"].strip().title()
    player["country"] = player["country"].strip().upper()

print("Original names:")
for player in players:
    print(repr(player["name"]))

print("Cleaned data:")
for player in cleaned_players:
    print(player["name"], player["team"], player["country"])

# The comprehension replaces a loop that copies and appends each player.
# Keeping the cleaning in a normal loop makes each change easy to follow.
