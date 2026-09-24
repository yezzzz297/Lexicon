
def classify_score(score):
    if score >= 60:
        return "PASS"
    return "FAIL"


print(classify_score(75))
print(classify_score(40))
