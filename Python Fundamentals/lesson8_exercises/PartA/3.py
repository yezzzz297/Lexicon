# Use None and create a new list

class Team:
    def __init__(self, name, members=None):
        self.name = name
        if members is None:
            members = []
        self.members = members

    def add_member(self, member):
        self.members.append(member)


team = Team("Python")
team.add_member("Ada")
print(team.members)
