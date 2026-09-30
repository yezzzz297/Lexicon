# Store different notification objects in one list

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
