# Each team has its own list

class Team:
    def __init__(self, name, members=None):
        self.name = name
        if members is None:
            members = []
        self.members = members

    def add_member(self, member):
        self.members.append(member)


team1 = Team("Python")
team2 = Team("AI")
team1.add_member("Ada")
print(team1.members)
print(team2.members)


# Only team1 contains Ada. Each team has a separate list.
