# Explain duck typing


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

# Both objects provide the method that this loop needs: display_status().
# They do not need a shared base class. This is called duck typing.
