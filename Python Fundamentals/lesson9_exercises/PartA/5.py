# Explain polymorphism


class EmailNotification:
    def send(self):
        return "Email sent!"


class SMSNotification:
    def send(self):
        return "SMS sent!"


class PushNotification:
    def send(self):
        return "Push notification sent!"


notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification(),
]

for notification in notifications:
    print(notification.send())

# The loop only needs each object to have a send() method.
# Python calls the version belonging to the current object.
# Do not need to check which notification class it comes from.
