# Give each class its own send() method

class EmailNotification:
    def send(self):
        return "Email sent!"


class SMSNotification:
    def send(self):
        return "SMS sent!"


class PushNotification:
    def send(self):
        return "Push notification sent!"

print(EmailNotification().send())
print(SMSNotification().send())
print(PushNotification().send())
