#Sessions longer than 45 minutes

for session in sessions:
    if session["minutes"] > 45:
        print(session)