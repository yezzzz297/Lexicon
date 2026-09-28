# Create two notification subclasses

class Notification:
    def send(self):
        return "Sending a notification."


class EmailNotification(Notification):
    pass


class SMSNotification(Notification):
    pass


email = EmailNotification()
sms = SMSNotification()
print(email.send())
print(sms.send())
