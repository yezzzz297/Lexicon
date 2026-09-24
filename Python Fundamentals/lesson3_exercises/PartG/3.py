#Total minutes per subject

subject_totals = {}

for session in sessions:
    subject = session["subject"]
    minutes = session["minutes"]

    if subject not in subject_totals:
        subject_totals[subject] = 0

    subject_totals[subject] += minutes

print(subject_totals)