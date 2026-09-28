# Override send in both subclasses

class Notification:
    def send(self):
        return "Sending a notification."


class EmailNotification(Notification):
    def send(self):
        return "Sending an email."


class SMSNotification(Notification):
    def send(self):
        return "Sending an SMS."


email = EmailNotification()
sms = SMSNotification()
print(email.send())
print(sms.send())
