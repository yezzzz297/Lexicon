# See the problem with a shared default list

class BadTeam:
    def __init__(self, name, members=[]):
        self.name = name
        self.members = members

    def add_member(self, member):
        self.members.append(member)


team1 = BadTeam("Python")
team2 = BadTeam("AI")
team1.add_member("Ada")
print(team1.members)
print(team2.members)


# Both teams show Ada because the default list is shared.
