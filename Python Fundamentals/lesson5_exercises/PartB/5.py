
def describe_scores(student_name, *scores):
    if not scores:
        return f"{student_name}: no scores available"

    total = 0
    for score in scores:
        total += score

    average = total / len(scores)
    return f"{student_name}: {len(scores)} scores, average = {average}"


print(describe_scores("Aisha", 80, 90, 100))
print(describe_scores("Ben"))
