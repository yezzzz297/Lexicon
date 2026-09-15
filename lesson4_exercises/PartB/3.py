
def classify_score(score):
    """Return PASS if the score is 60 or more."""
    if score >= 60:
        return "PASS"
    return "FAIL"


print(classify_score(75))
print(classify_score(40))
