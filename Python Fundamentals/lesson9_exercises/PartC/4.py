# Call display_status() on each object

class Printer:
    def display_status(self):
        return "Printer is ready"


class Screen:
    def display_status(self):
        return "Screen is on"


devices = [
    Printer(),
    Screen(),
]

for device in devices:
    print(device.display_status())
