# Give both classes display_status()

class Printer:
    def display_status(self):
        return "Printer is ready"


class Screen:
    def display_status(self):
        return "Screen is on"


print(Printer().display_status())
print(Screen().display_status())
