
scores = [78, 90, 64, 88, 92]
print("Has score above 90?", any(score > 90 for score in scores))
print("Are all scores above 50?", all(score > 50 for score in scores))
