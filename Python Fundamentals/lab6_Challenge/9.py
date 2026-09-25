# Part 9 - Performance

# Cleaned data from Part 2; included here so this file runs on its own.
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

# A win adds 10 points. 
performance_players = []
for player in players:
    new_player = player.copy()
    new_player["performance"] = player["score"] + player["wins"] * 10
    performance_players.append(new_player)

ranking = sorted(performance_players, key=lambda player: player["performance"], reverse=True)
top_players = ranking[:5]
above_threshold = [player for player in ranking if player["performance"] > 130]
performance = {player["name"]: player["performance"] for player in performance_players}

print("Performance ranking:")
for rank, player in enumerate(ranking, start=1):
    print(rank, player["name"], player["performance"])

print("Top 5:", [player["name"] for player in top_players])
print("Above 130:", [player["name"] for player in above_threshold])
print("Performance values:", performance)
