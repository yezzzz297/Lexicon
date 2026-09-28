# A mutable default list (intentionally incorrect)

class BadTeam:
    def __init__(self, name, members=[]):
        self.name = name
        self.members = members

    def add_member(self, member):
        self.members.append(member)


team = BadTeam("Python")
team.add_member("Ada")
print(team.members)
