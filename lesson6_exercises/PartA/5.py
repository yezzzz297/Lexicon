
scores = [54, 49, 80, 42, 67]
labels = ["PASS" if score >= 50 else "FAIL" for score in scores]
print(labels)
